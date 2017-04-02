import sys
def makegood(x):
    while x<-128:
        x+=256
    while x>127:
        x-=256
    return x


if len(sys.argv)<2:
    print("Please give a filename")
else:
    if len(sys.argv)>2:
        program=list(sys.argv[1])
    else:
        f = open(sys.argv[1],'r')
        program = f.read().split('\n')
        for i in range(len(program)):
            program[i]=program[i].count('o')
        f.close()
array = [0 for i in range(100)]
pointer=0
prgpointer=0
run = True
while run:
    try:
        
        command = program[prgpointer]
        if command == 1: #>
            pointer += 1
        if command == 2: #<
            pointer -= 1
        if command == 3: #+
            array[pointer]=array[pointer]+1
        if command == 4: #-
            array[pointer]=array[pointer]-1
        if command == 5: #.
            sys.stdout.write(chr(array[pointer]))
        if command == 6: #,
            array[pointer]=input('>')
        if array[pointer]>127:
            array[pointer]-=256
        if array[pointer]<-128:
            array[pointer]+=256
        if command == 7 and array[pointer]==0: #[
            stack = 1
            while stack!=0:
                prgpointer+=1
                if program[prgpointer]==7: #[
                    stack+=1
                if program[prgpointer]==8: #]
                    stack-=1
        if command == 8 and array[pointer]!=0: #]
            stack = 1
            while stack!=0:
                prgpointer-=1
                if program[prgpointer]==8: #]
                    stack+=1
                if program[prgpointer]==7: #[
                    stack-=1       
    except:
        run = False  
    prgpointer+=1
