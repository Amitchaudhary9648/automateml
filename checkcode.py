#connecting to the code file
programfile = open('/home/jyotirmaya/ws/mlops1/program.py','r')

#reading the code file
code = programfile.read()				

#because keras or tensorflow keyword is a cmust have for a dl program
if 'keras' or 'tensorflow' in code:
    #beacuse if a code is of CNN conv2D layer is a must have
    if 'Conv2D' in code:
        print('kerasCNN')
    else:
        print('not kerasCNN')
else:
    print('not deep learning')
