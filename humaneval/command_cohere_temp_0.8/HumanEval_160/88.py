Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly
    exp_op = operator.pop() if operator else None
    if exp_op:
        operand = [x ** y for x, y in zip(operand, operator)]

    for op in operator:
        result += operand[0] * algebra[op]
        operand = operand[1:]

    # If there was an exponentiation operator, handle it now
    if exp_op:
        result += operand[0] if operand else 0
    return result

# Mapping of basic algebra operations
algebra = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '//': lambda x, y: x // y if y != 0 else float('inf'),
    '**': lambda x, y: x ** y
}
```

This code defines a function `do_algebra` that takes in two parameters, `operator` and `operand`. It uses the `algebra` dictionary to perform the appropriate operation on the operands based on the provided operator. The function handles exponentiation separately, and the remaining operations are performed using a generator expression. The resulting value is returned. 

The code assumes that the length of the `operator` list is equal to the length of the `operand` list minus one. It also assumes that the `operand` list contains non-negative integers and that the `operator` list contains at least one operator and the `operand` list has at least two operands. 

Note that this code assumes that the data type of the operand is an integer and may need to be adjusted accordingly if the data type is different.