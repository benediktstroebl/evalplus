Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = ''
    
    for i in range(num_operands):
        if i > 0: 
            expression += ' ' + operator[i-1] + ' '
        expression += str(operand[i])
    
    return eval(expression)
```
This script defines a function `do_algebra` that takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the provided operator and operand.

The function runs through the elements of the `operand` list, and for each element that is not the first, it adds the corresponding element of the `operator` list to form an expression. The expression is then evaluated using the `eval` function. 

This solution tests successfully against the provided unit tests. Let me know if you'd like me to make any additional clarifications or provide further contextual information!