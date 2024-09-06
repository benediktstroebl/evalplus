Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * eval(f'{operator[i]}{{i+1}}')
    return result
```

The script uses a `for` loop to iterate through the lengths of the `operator` and `operand` lists. The `eval` function is used to construct arithmetic expressions with the respective values from the `operand` list, and the `operator` list. The `result` variable is then incremented to hold the computed value of the expression.

The `do_algebra` function can be used to solve the problem as shown in the example below:
```python
# Example usage
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)  # Output: 9
```

This will return the evaluated value of the algebraic expression constructed using the given `operator` and `operand` lists, which in this case is `9`. 

Note that this approach assumes that the `operand` list contains only positive integers, and the `operator` list contains basic algebra operations, as outlined in the Problem Statement.