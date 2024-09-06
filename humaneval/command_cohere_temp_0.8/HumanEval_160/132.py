Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Calculate result using binary right evaluation
    for i in range(len(operand) - 1):
        # Calculate the current element in the expression
        element_result = operand[i] + operator[i] * operand[i + 1]
        # Update the result with the latest evaluated expression
        result += element_result
    return result
```

The following steps illustrate how the algorithm works:
1. Iterate through the length of the operand list minus one, this is to ensure that each operator is paired correctly with its operand.
2. In each iteration, an element of the resulting expression is calculated by adding the corresponding operator and its operands, this is done using integer multiplication and addition.
3. Finally, the result of the expression is returned.

This algorithm follows a simple approach using binary right evaluation to calculate the resulting expression with the provided operator and operand list.

The function do_algebra works with both primitive data types of lists and integers, making it a self-contained algorithm to solve the given problem. It returns the computed result after fully evaluating the algebraic expression constructed from the provided operator and operand lists.