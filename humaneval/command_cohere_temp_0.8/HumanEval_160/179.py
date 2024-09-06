Here's a Python script that solves the problem with a self-contained function:
```python
def do_algebra(operator, operand):
    result = 0
    # Using loop to handle multiple elements in the operation
    for i in range(len(operand)):
        for oper in operator:
            # Handling exponentiation
            if oper == "**":
                result = result * operand[i] ** oper
              # Handling rest of the operations
            else:
                result = result * oper(operand[i])
    return result
```
The script uses a nested loop to iterate over the operands and operators and efficiently builds the expression.

To expound upon the logic being used here, each iteration of the outer loop fetches an operand for the current expression being built, and the inner loop selects the operation to perform on the operand. 

Then the script iterates over each operand in the expression and applies the corresponding operator, after which it returns the final value of the expression which is the value of the 'result' variable. 

This solution is efficient and can solve the problem in an optimal number of steps.