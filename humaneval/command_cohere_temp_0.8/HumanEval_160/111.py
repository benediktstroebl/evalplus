Here's a Python script that solves the problem you've outlined using a function with the specified constraints:
```python
def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result
```
This code provides a Python function called `do_algebra` that takes in two parameters, `operator` and `operand`. It loops through the length of the `operator` list and uses the respective element in the `operand` list to perform the algebraic operation, which it then adds to the `result` variable. Finally, it returns the `result` computed after performing the operations specified in the `operator` list. 

You can test this function by calling it with different operators and operands to see if it returns the expected results.