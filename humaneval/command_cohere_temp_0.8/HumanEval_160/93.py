Here's a Python script that solves the problem you've outlined using a function called `do_algebra`:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate over it twice
    n = min(len(operator), len(operand)) - 1
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{operand[i+1]}')
    return result
```

This script defines a Python function called `do_algebra`. This function takes two lists, `operator` and `operand`, as input. It iterates over the lists, calculating the expression at each step and returning the final result after all expressions have been calculated. 

Note that this function assumes that the lists have valid lengths and necessary operations, as specified in the problem description. It also assumes that the operand list contains non-negative integers.