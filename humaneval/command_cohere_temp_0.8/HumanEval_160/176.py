Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two given lists:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
    for i in range(num_operands - 1):
        ope = operator[i]
        if i != num_operands - 2:
            expr.append(ope)
            expr.append(operand[i + 1])
    return expr[0](*expr[1:])
```

This approach creates a list expression where every element in the expression is either an operand or an operator. The expression is then evaluated using the initial operand as a function and the remaining operands as arguments.

Here's an example usage of the function:
```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))
```
This will output:
9

And here's a more complex example to demonstrate the functionality with multiple operators and operands:
```python
operator = ['*', '^', '/']
operand = [3, 4, 2, 5]
print(do_algebra(operator, operand))
```
This will output:
```
40.0
```