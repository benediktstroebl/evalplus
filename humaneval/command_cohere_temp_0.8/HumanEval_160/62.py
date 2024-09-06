Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using the provided operations and operands
    for i in range(len(operand) - 1):
        result += operand[i] + operator.index(operator[i]) * operand[i + 1]
    result += operand[-1]

    # Remove the last operand since it was added twice
    return result - operand[-1]
```

The function works by converting the algebraic expression described by the `operator` and `operand` lists into a numeric value. It iterates over the elements of the `operand` list, using the index of the `operator` list as a lookup to determine the correct arithmetic operation to perform. The result is computed by adding the accumulated result with the last operand separately at the end to account for the doubled term, and then subtracting to get the correct result. 

This approach avoids explicitly defining an expression string, making the function more self-contained without relying on string concatenation.  Relative to traditional approaches that use `join` to concatenate a list of operators, this function has a **time complexity` of O(n), where n is the length of the `operand` list, and a `space complexity` of O(1) since it only requires a single counter variable to be stored.