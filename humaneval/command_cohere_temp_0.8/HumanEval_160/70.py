Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate 3 times
    n = min(len(operator), len(operand))
    for i in range(n):
        result += operand[i] * eval(f'{operator[i]}{{result}}')
    return result
```

This script defines a function `do_algebra` that takes two lists, `operator` and `operand`, as input. It iterates over the shorter of the two lists and uses the elements from both lists to construct arithmetic operations, evaluating them using the `eval` function and keeping a running total of the results. The function then returns the final result.

Keep in mind that the `eval` function should be used with caution, as it can execute arbitrary code and pose security risks when handling untrusted data. In this case, since we're constructing the expressions ourselves and using a predefined set of operators, the risk is relatively low, but it's still good practice to be mindful of its usage.