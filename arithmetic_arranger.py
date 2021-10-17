def arithmetic_arranger(problems):

    largo = len(problems)
    arranged_problems = [""] * largo
    
    for i in range(0,largo):
        arranged_problems[i]  = problems[i].split(" ")

    if(largo > 5):
        return "Error: Too many problems."

    for i in arranged_problems:
        if(i[1] !='-' and i[1]!='+'):
            return "Error: Operator must be '+' or '-'."
        try:
            int(i[0])
            int(i[2])
        except:    
            return "Error: Numbers must only contain digits."                            
        if(int(i[0])>9999 or int(i[2])>9999):    
            return "Error: Numbers cannot be more than four digits."


    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for j in arranged_problems:
        num1 = j[0]
        num2 = j[2]
        ope = j[1]
        largoCuenta = max(len(num1), len(num2))+2
        line1 = line1 + " " * (largoCuenta-len(num1)) + num1 + " " * 4
        line2 = line2 + ope + " " * (largoCuenta-len(num2)-1) + num2 + " " * 4
        line3 = line3 + "-" * (largoCuenta) + " " * 4

        
        result = int(num1)+int(num2)
        long = len(str(result))
        line4 = line4 + " " * (largoCuenta-long) + str(result) +  " " * 4

    
    
    if(displayResults):
        print(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 )
    else:
            print(line1 + "\n" + line2 + "\n" + line3)    
