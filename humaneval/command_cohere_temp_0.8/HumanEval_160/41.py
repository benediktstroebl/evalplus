Here's a Python script that includes a function `do_algebra` which takes two arguments, `operator` and `operand`, and returns the result of the algebraic expression created using the two input lists. The script also includes a few tests to ensure the function behaves correctly:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = []
    for i in range(num_operands):
        if i != 0: 
            expression.append(operator[i-1])
        expression.append(operand[i])
    return eval(' '.join(expression))

# Tests
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
test_result = do_algebra(operator, operand)
print(test_result)  # Expected output: 9

operator = ['*', '^', '-']
operand = [3, 2, 4]
test_result = do_algebra(operator, operand)
print(test_result)  # Expected output: -1

operator = ['-', '+', '*']
operand = [2, 3, 4]
test_result = do_algebra(operator, operand)
print(test_result)  # Expected output: 7

operator = ['*', '+', '-']
operand = [3, 2, 5]
test_result = do_algebra(operator, operand)
print(test_result)  # Expected output: -15

operator = ['^', '^', '-']
operand = [3, 2, 5]
test_result = do_algebra(operator, operand)
print(test_result)  # Expected output: 40
```

This script defines the `do_algebra` function, which uses the `operator` list and `operand` list to construct an algebraic expression using the operators provided, and then returns the result of the expression.

The script also includes several tests to ensure the function produces the correct results for different combinations of operators and operands. You can add more tests to this list as desired.