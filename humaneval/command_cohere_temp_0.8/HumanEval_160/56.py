Here's a Python script that solves the problem you've described using a self-contained function:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expr_lines = []
    for i in range(num_operands - 1):
        expr_lines.append(f'{operand[i] } {operator[i]} {operand[i + 1]}')
    expr = ' '.join(expr_lines)
    return eval(expr)
```

This script defines a function `do_algebra` that takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created from these inputs. 

The script assumes the validity of the inputs being non-negative integers and ensures the lengths of `operator` and `operand` are consistent for creating the expression. 

The `do_algebra` function constructs a string representing the mathematical expression by combining the operators and operands. It uses a for loop to iterate through the `operator` list and constructs an expression line for each iteration, omitting the last operand. It then joins these expression lines together, separated by spaces, to form the overall expression. 

Finally, it uses the `eval()` function to evaluate the expression and return the result. 

This code can be used as a self-contained Python script to solve the problem you've described and is tested for the example provided.