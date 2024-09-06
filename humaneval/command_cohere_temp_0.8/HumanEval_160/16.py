Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands):
        if i != 0:
            expr.append(operator[i-1])
        expr.append(operand[i])
    return eval(' '.join(expr))
```

The algorithm works as follows:
1. The length of the `operand` list is calculated and stored in the `num_operands` variable.
2. An empty list named `expr` is created to store the algebraic expression.
3. The algorithm loops `num_operands` times, adding an operator from the `operator` list to `expr` if it's not the first iteration (index != 0).
4. Subsequently, an element from the `operand` list is appended to `expr`. 
5. Finally, the expression is formed by joining the elements of `expr` using spaces, and is evaluated using the `eval` function. 

This approach ensures that the algebraic expression is correctly built and evaluated using the provided operator and operand lists.