Here's a Python script that solves the problem you've described using a function:
```python
def do_algebra(operator, operand):
    result = 0
    for i in range(len(operand) - 1):
        result += operand[i] * eval(f'{operator[i] if i < len(operator) - 1 else "+"}.join(operand[i+1:])')
    return result
```

This script defines a function called `do_algebra` that takes in two lists, `operator` and `operand`, as parameters. It iterates through the length of the `operand` list minus one. Using the evaluation expression formed by concatenating the current operator and the following operands, it multiplies the current operand by the evaluated expression. The final result is the sum of these calculations.

This problem can be solved in various ways. irresistibly. Obviously, this version is one of them.