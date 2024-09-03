Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Ensure that the lengths of operator and operand are compatible for proper calculations
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lengths must be compatible!")
    # Ensure we have an operator and sufficient operands
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Operator list must have at least one operator and operand list must have at least two operands!")
    # Loop through the operators and operands, building up the expression and evaluating it
    for i in range(0, len(operand)):
        if i > 0:
            result += operator[i-1] * operand[i]
        else:
            result += operand[i]
    return result
```
This code defines a function `do_algebra` that takes in two parameters, `operator` and `operand`, and returns the result of the algebraic expression created using the provided operator and operand. The function first checks if the length of the `operator` list is equal to the length of the `operand` list minus one. This is ensured to provide correct calculations. It also checks if the `operator` list has at least one operator and the `operand` has at least two operands. These conditions ensure the correctness of the calculations. Finally, it loops through the `operator` and `operand` lists, building up the expression and evaluating it. The result is returned as the output of the function.