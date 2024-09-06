Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation separately, as it needs to be iterated through both lists
    exponentiation_result = [operand[0] ** operand[1]] if '**' in operator else []

    for op in operator:
        if   op == '+': result += operand[0]
        elif op == '-': result -= operand[0]
        elif op == '*': result *= operand[0]
        elif op == '//': result //= operand[0]
        elif op == '**': exponentiation_result.append(operand[0] ** operand[1])
        operand = [operand[1]] if op == '**' else operand[1:]

    return result + exponentiation_result[0] if exponentiation_result else result
```

This script defines a function `do_algebra` that takes two lists, `operator` and `operand`, as input and returns the result of the algebraic expression created based on the given lists. The function handles each operation separately, and then iterates through the `operator` list and executes the relevant mathematical operation on the corresponding elements in the `operand` list. Finally, the result of each operation is returned. 

Note: the handling of the exponentiation operation `**` is treated separately and an empty list `exponentiation_result` is initialized before the loop to handle the operation, as it needs to iterate through the `operand` list only once.