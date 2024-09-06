Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly, as it needs to be iterated through differently
    exp_op = operator.count('**')
    if exp_op > 0:
        for i in range(len(operand) - 1):
            result += operand[i] ** operand[i + 1]
    else:
        for i in range(len(operand) - 1):
            if operator[i] == '+':
                result += operand[i] + operand[i + 1]
            elif operator[i] == '-':
                result += operand[i] - operand[i + 1]
            elif operator[i] == '*':
                result += operand[i] * operand[i + 1]
            else:  # // case
                result += operand[i] // operand[i + 1]
    return result
```
This script takes two inputs: a list of operators and a list of operands. It then returns the result of the algebraic expression formed using the given operators and operands. The script handles both exponentiation and basic algebra operations, using nested loops to pair the operands with the correct operators. The result is then returned as the solution to the algebraic expression.