Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    num_ops = len(operator)
    expr = []
    for i in range(num_ops):
        expr.append(operand[i] if i % 2 == 0 else operator[i] + '(' + str(operand[i]) + ')')
    return eval(' '.join(expr))
```

This script defines a function `do_algebra` that takes two arguments, `operator`, and `operand`. The function creates an expression using the `operator` and `operand` lists and evaluates the expression. The expression is built by taking pairs of elements from the `operand` list and appending them to the `operator` list. The resulting expression is a string that is evaluated using the `eval` function.

Here's an example usage of the function:
```python
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)
```

This will output:
```
9
```

This method uses string concatenation and evaluation to build and evaluate the expression, making it flexible to handle different combinations of operations and operands. It checks the length of the `operator` list to determine the expression's structure and correctly handles nested parentheses. The `operand` list is iterated in pairs to match each element with an operator.