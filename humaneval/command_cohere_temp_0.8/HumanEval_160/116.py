Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists. The script also includes a set of tests to ensure the function behaves as expected:
```python
def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = ""
    
    # Ensure that the maximum number of operands is used.
    # If the length of operator list is less than the length of operand list, 
    # extend the operator list with '*' so the length of the two lists is the same.
    if len(operator) < num_operands:
        operator += ['*'] * (num_operands - len(operator))

    for i in range(num_operands - 1):
        expression += str(operand[i]) + ' ' + operator[i] + ' '

    # Add the last operand to the expression without a separator
    expression += str(operand[-1])
    
    return eval(expression)

# Tests
# All the below tests assume that the length of operator list is less than the length of operand list, 
# so the operator list is extended with '*' 

# Test 1
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
expectation = 9
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 1.")

# Test 2
operator = ['-', '*']
operand = [3, 4, 5, 6]
expectation = -24
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 2.")

# Test 3
operator = ['+', '-', '*']
operand = [2, 3, 4, 8]
expectation = 17
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 3.")

# Test 4
operator = ['*', '-', '+']
operand = [3, 4, 5, 2]
expectation = -10
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 4.")

# Test 5
operator = ['+', '*', '*', '-']
operand = [1, 2, 3, 4, 5]
expectation = -5
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 5.")

# Test 6
operator = ['-', '**', '+', '*']
operand = [2, 3, 4, 5]
expectation = -28
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 6.")

# Test 7
operator = ['*', '+', '-', '**']
operand = [2, 3, 4, 5]
expectation = -20
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 7.")

# Test 8
operator = ['+', '**', '-', '*']
operand = [1, 2, 3, 4]
expectation = 10
result = do_algebra(operator, operand)
test_eq(result, expectation, "Failed test 8.")

# Test 9
operator = ['-', '*', '**', '+']
operand = [1, 2, 3, 4]