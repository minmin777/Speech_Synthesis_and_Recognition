#build an FST that converts the color names in
#minidictionary.txt to their phonetic representations
from FSA_FSM_HMM import *
f = open('minidictionary.txt', 'r')
dic_list = []
list_of_words = []
for line in f:
    dic = {}
    s = line.split()
    dic[s[0]] = s[1:]
    list_of_words.append([s[0]])
    dic_list.append(dic)

dic_list = dic_list[1:]

#print dic_list

start_state = 0
inputal = set([])
outputal = set([])
st = set([])
final = set([])
transition = {}
state = 1
for i in dic_list:
    for j in i:
        if len(i[j]) != len(j):
            i[j].append('')
        for k in range(len(j)):
            inputal.add(j[k]) #j[k] for 'red'
            outputal.add(i[j][k]) #i[j][k] is ['R', 'EH', 'D']
            st.add(state)
            if k == len(j) - 1:
                final.add(state)
            if k == 0 and transition.get((0, j[k]), "") == "":
                transition[(0, j[k])] = (i[j][k], state)
                state += 1
                #print transition[(0, j[k])]
                
            elif k == 0 and transition.get((0, j[k]), "") != "":
                value = transition[(0, j[k])][1]
                transition[(value, j[k+1])] = (i[j][k+1], state)
                
                continue
            else:
            #print "else" , (state-1, j[k]), (i[j][k], state), state
                transition[(state-1, j[k])] = (i[j][k], state)
                state += 1
        

           
#print inputal , outputal
#print "this is the transition dic: \n"
#print final , "\n"

#for key in transition:
#    print transition[key]

dictionary1 = FST(inputal, outputal, st, 0, final, transition)
dictionary1.finalfst("amber")
#dictionary1.finalfst(word)
for word in list_of_words[1:]:
    print dictionary1.finalfst(str(word[0]))



                        
                    
        

