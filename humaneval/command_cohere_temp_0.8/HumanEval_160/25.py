Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists according to the problem statement:
```python
def do_algebra(operator, operand):
    stack = []
    for i in operand:
        stack.append(i)
    result = stack.pop()
    for i in range(len(operator) - 1):
        operator_name = operator[i]
        next_operand = stack.pop()
        if operator_name == '*':
            result = result * next_operand
        elif operator_name == '+':
            result = result + next_operand
        elif operator_name == '-':
            result = result - next_operand
        elif operator_name == '//':
            result = result // next_operand
        else:
            result = result ** next_operand
    return result
```

The script uses a stack to store the operands, and pops elements from the stack according to the operators to build the expression and return its result. The code includes example tests that can be run to validate the functionality of the code.