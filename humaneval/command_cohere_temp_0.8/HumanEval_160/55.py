Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    num_ops = len(operator)
    expr = []
    for i in range(num_ops):
        expr.append(operand[i] if i % 2 == 0 else operator[i] + '(' + str(operand[i]) + ')')
    return eval(' '.join(expr))
```

This script defines a function `do_algebra` that takes two arguments, `operator`, and `operand`. The function creates an expression using the operands and operators provided, respecting the operator's order and casting operands into parentheses. Finally, the function evaluates the expression and returns the result.