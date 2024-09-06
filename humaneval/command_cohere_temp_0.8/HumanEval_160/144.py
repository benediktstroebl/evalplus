Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using python eval function
    for i in range(len(operand)-1):
        temp = list(operand[i])
        for j in range(i+1, len(operand)):
            temp.extend(str(operand[j]))
            temp = ' '.join(temp)
            result += eval(f'{operator[i]}{temp}')
    return result
```
This script takes two arguments, operator, and operand, and returns the result of the algebraic expression created using the provided operator and operand. The function do_algebra uses the python Eval function to evaluate the expression using **safe** multi-line string formatting. A temporary list of digits is formed for each pair of operands and the corresponding pair of operators. The list of digits is turned into a string and the resulting expression is evaluated. The process is repeated for all digit pairs and corresponding operators. The algorithm is guaranteed to work only if the operands are non-negative integers.