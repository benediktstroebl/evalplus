Here's a Python script that solves the problem you've described using a self-contained function:
```python
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
```

This script takes two inputs: `operator`, which is a list of algebraic operations, and `operand`, which is a list of integers. It uses these inputs to build an algebraic expression and returns the expression's evaluation. 

The function employs a nested loop structure that operates on elements from the arrays. It iterates through all possible combinations of operands and algebraic operations, using the corresponding element from the `operator` list. 

The function complies with the constraints provided in the prompt by taking a len(operand) - 1 times len(operand) - 1 times len(operand) - 1 approach. The idea behind this approach is that for each element in the first operand list, we pair it with every element in the second operand list, and then also consider the third element in the operand list, which is analogous to a triple nested loop. 

The resulting evaluation of the algebraic expression is returned as a list, where the first element is the result of the expression.

This code assumes that the input lists are well-formed and the algebraic operations are valid. It does not perform any input validation or error checking.