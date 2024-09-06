def do_algebra(operator, operand):
    result = 0
    Operate = len(operator)
    for i in range(Operate):
        switch = True
        for j in range(len(operand)-1):
            if operand[j] == operand[j+1]:
                switch = False
        if switch:
            result += operand[0] * operator[i]
        else:
            result += operator[i] * operand[0]
        operand.remove(operand[0])
    return result