Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate over it twice
    n = min(len(operator), len(operand)) - 1
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{operand[i+1]}')
    return result
```

This script defines a function `do_algebra` that takes two lists, `operator` and `operand`, as input. It iterates over the two lists simultaneously, with a loop index moving twice for the length of the shorter list. During each iteration, it adds the product of two consecutive elements from the `operand` list, assuming the operators between them require multiplication. It then returns the final result after all the iterations.

Note: This approach assumes the `operand` list contains only positive integers and that the `operator` list contains only valid mathematical operations.