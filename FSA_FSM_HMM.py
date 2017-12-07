import operator

def get_transition(current, dic):
                bro = dic
                return bro.get(current,None)
class FSA: #This FSA takes any string and will be True if it has at least one a
        def __init__(self, alphabet, state, initialstate, finalstate, transition):
                self.al = alphabet
                self.st = state
                self.initial = initialstate
                self.final = finalstate
                self.transition = transition
        

        def finalfsa(self, string):
                get = get_transition((self.initial, string[0]), self.transition)
                for c in range(1, len(string)):
                        pair = (get, string[c])
                        get = get_transition(pair, self.transition)
                if get == None:
                    return False
                elif get in self.final:
                    return True
                else:
                    return False

class FST: #This FST changes the first 'a' to an 'e'
        def __init__(self, inputal, outputal, state, initialstate, finalstate, transition):
                self.inp = inputal
                self.out = outputal
                self.st = state
                self.initial = initialstate
                self.final = finalstate
                self.transition = transition
        
        def finalfst(self, string):
                get = get_transition((self.initial, string[0]), self.transition)
                str2 = get[0]
                for c in range(1, len(string)):
                    get = get_transition((get[1], string[c]), self.transition)
                    #if get[1] in self.final:
                    str2 += get[0]
                return str2
                                

hello1 = FSA({'a','b'}, {0,1}, 0, set([1]), {(0,'b'):0, (0, 'a'):1, (1,'a'):1, (1,'b'):1}) #example from class: takes 
print hello1.finalfsa("b")

hello2 = FSA({'a','b'}, {0,1}, 0, set([1]), {(0,'b'):0, (0, 'a'):1, (1,'a'):1, (1,'b'):1}) #example from class: takes 
print hello2.finalfsa("ababa")

hello3 = FSA({'a','b'}, {0,1}, 0, set([1]), {(0,'b'):0, (1,'a'):1, (1,'b'):1}) #example when there's no transition to the next state
print hello3.finalfsa("aba")

bro = FST(set(['a','b']), set(['a','b']), set([0, 1]), 0, set([0, 1]), {(0, 'b'):('b', 0), (0, 'a'):('e', 1), (1,'a'):('a', 1),(1,'b'):('b', 1)})
print bro.finalfst("aba")




class HMM:
    global get_state_sequence_prob
    def __init__(self, states, transitionprob, observationprob):
 #       self.start = start;
        self.state = states;
        self.transition = transitionprob #tuple
        self.observation = observationprob #tuple
    def get_state_sequence_prob(self, alist):
        probability = 1
        for c in range(len(alist)-1):
            get = get_transition((alist[c], alist[c+1]), self)
            probability *= get
        return probability

    def veterbi(self, observation):
  #      dic = {}
        num = 1
        dic_list = []
        for c in self.state:
            dic= {}
            vet1 = get_state_sequence_prob(self.transition, ('start', c))* get_transition((c,observation[0]), self.observation)
            string = ('start'),(c)
            #dic_name = 'dic' + str(num)
            dic[string] = vet1
            dic_list.append(dic)
        for o in range(1, len(observation)):
            for k in range(len(dic_list)):
                string2 = dic_list[k].keys()[0]
                num3 = dic_list[k][string2]
                del dic_list[k][string2]
                for l in self.state:   
                    string3 = string2+(l,)
                    num2 = num3*get_state_sequence_prob(self.transition, (string3[-2], string3[-1]))*get_transition((l, observation[o]), self.observation)
                    dic_list[k][string3] = num2
                key = min(dic_list[k].iteritems(), key=operator.itemgetter(1))[0]
                del dic_list[k][key]
        max_num = max(xrange(len(dic_list)), key=lambda index: dic_list[index])
        return dic_list[max_num]
                    
                    
hmm = HMM(('H', 'C'), {('start', 'H'):.8, ('start', 'C'):.2, ('H', 'H'):.7, ('H', 'C'):.3, ('C', 'H'):.4, ('C', 'C'):.6}, {('H', 1):.2, ('H', 2):.4, ('H', 3):.4, ('C', 1):.5, ('C', 2):.4, ('C', 3):.1})
#print hmm.get_state_sequence_prob(('start', 'C', 'H', 'H'))
print hmm.veterbi([2, 3])
print hmm.veterbi([1,2,3])

           


		
		
	
		

