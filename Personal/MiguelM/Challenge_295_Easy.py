def Transform(input1, input2):
    currentString = input1
    print(input1)
    for i in range (len(input1)): #for(int i = 0; i < len(input1); i++)
        if(input1[i] != input2[i]):
            #string slice notation, have to add +1 becuase syntax is i-1
            currentString = input2[:i+1] + input1[i+1:] 
            print(currentString)
