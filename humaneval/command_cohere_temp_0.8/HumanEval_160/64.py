Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using chained operations
    for i in range(len(operand) - 1):
        result = operand[i] + operator[i] * result
        if i != len(operand) - 2:
            result = result + operand[i + 1]
    return result
```

This script defines a function `do_algebra` that takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression formed from the given operator and operand. The function iterates over the length of the `operand` list minus 1, using the current element in the `operand` list and the `operator` list to form an expression. It then updates the `result` variable with the evaluation of this expression, and the next element in the `operand` list. The process continues until the iteration is complete, returning the final value of `result` as the result of the algebraic expression.

This script assumes that the `operand` list contains at least two elements and that the `operator` list contains at least one element. These are important assumptions as the length of the `operator` list equals the length of the `operand` list minus one. It also assumes that the `operand` list contains only non-negative integers. 

The function is designed to be self-contained and does not rely on any external variables or functions. 

It is important to note that this script assumes that the elements in the `operand` list are correctly populated and are of the correct data type, namely integers. 

You can test this function by calling it with a variety of operator and operand lists and verifying that the output matches the expected result.