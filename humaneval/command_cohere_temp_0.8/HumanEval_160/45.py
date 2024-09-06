Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to subtract from the length of the longer list
    n = min(len(operator), len(operand)) - 1
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{operand[i+1]}')
    return result
```

This script takes two lists, operator, and operand, as input. It follows the specified order of operations from the operator list and uses the eval function to evaluate the expression by passing the string representation of the expression as an argument. It then returns the final result after calculating all the operations in the expression.

It assumes that the operator list contains only basic algebra operations (+, -, *, //, **) and that the operand list contains only non-negative integers. If these preconditions are not met, the function may not return the expected results.