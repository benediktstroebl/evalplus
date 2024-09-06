def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            operand_ij = operand[i]
            for k in range(j + 1, len(operand)):
                operand_jk = operand[j]
                operand_ik = operand[k]
                for o in range(len(operator)):
                    if operator[o] == '+':
                        stack.append(operand_ij + operand_jk + operand_ik)
                    elif operator[o] == '-':
                        stack.append(operand_ij - operand_jk - operand_ik)
                    elif operator[o] == '*':
                        stack.append(operand_ij * operand_jk * operand_ik)
                    elif operator[o] == '**':
                        stack.append(operand_ij ** operand_jk ** operand_ik)
                    elif operator[o] == '/':
                        stack.append(operand_ij // operand_jk // operand_ik)
    return stack[0]