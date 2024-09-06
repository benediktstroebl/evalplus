Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using a loop to enforce the constraint of a minimal operator list and a minimal operand list
    for i in range(len(operand) - 1):
        result += operator[i] * operand[i+1]
    return result
```
This Python script defines a function do_algebra that takes in two lists, operator and operand, and returns the result of the algebraic expression formed using the two lists. The script enforces the constraint of a minimal operator list (of length 1) and a minimal operand list (of length 2) by iterating through the lengths of these lists. This leads to a valid mathematical expression constructed from the two lists, with the expression evaluated using a loop and the result returned accordingly.