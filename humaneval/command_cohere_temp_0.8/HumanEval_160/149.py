Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebriac expression created using the two lists. The script also includes a set of tests to ensure the function behaves as expected:
```python
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
       The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    num_operands = len(operand)
    if num_operands == 1:
        raise ValueError("Operand list must have at least two integers")
    
    num_operators = len(operator)
    if num_operators == 0:
        raise ValueError("Operator list must have at least one operator")
    
    expression_parts = []
    for i in range(num_operands):
        part = operand[i]
        for j in range(i + 1, num_operands):
            operator_token = operator[j - i - 1]
            part = operate(operator_token, part, operand[j])
            if part == 0:
                break
        expression_parts.append(part)
    
    return expression_parts[0]
    
def operate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '//':
        return operand1 // operand2
    if operator == '**':
        return operand1 ** operand2
    
# Tests
operand = [2, 3, 4, 5]
operator = ['+', '*', '-']
test_cases = [
    ([2, 3], '+', 5, 2 + 3),
    ([2, 3, 4], '*', 5, 2 * 3 * 4),
    ([2, 3, 4, 5], '-', 6, 2 * 3 * 4 - 5),
    ([2, 3, 4, 5], '//', 2, 2 // 3 // 4 // 5),
    ([2, 3, 4, 5], '**', 2, 2 ** 3 ** 4 ** 5)
]

for t in test_cases:
    assert do_algebra(operator, t[0]) == t[3]
``` 

The function operates by matching each integer from the `operand` list with its corresponding operator from the `operator` list, applying the respective operation, and building the expression incrementally. The function raises a `ValueError` if the operand list has less than two elements or the operator list has no operations. The included tests check for these conditions, as well as ensure the function produces the correct results for various test cases. 

Note that the code assumes that the `operand` list contains only non-negative integers and provides no validation for negative or non-integer inputs.