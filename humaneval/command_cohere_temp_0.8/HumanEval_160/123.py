Here's a Python script that includes a function `do_algebra` which takes two lists, `operator` and `operand`, and returns the result of the algebraic expression created using the two lists:
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
    size = len(operand)
    if size == 1:
        return operand[0]
    expression = []
    for i in range(size):
        if i == 0:
            expression.append(operand[i] + operand[i+1])
        elif i == size - 1:
            expression.append(operand[i-1] * operand[i])
        else:
            expression.append(operand[i-1] * operand[i] + operand[i+1] + operand[i+2])
    for sign, op in enumerate(operator):
        if op == '*':
            expression[sign] = expression[sign] * 2
        elif op == '//':
            expression[sign] = expression[sign] // 2
        elif op == '+':
            expression[sign] = expression[sign] // 2 + expression[sign+1]
        elif op == '-':
            expression[sign] = expression[sign] // 2 - expression[sign+1]
        elif op == '**':
            expression[sign] = expression[sign] ** 2
    return expression[0]
```

The script includes a test class with a few test scenarios to cover different scenarios of the function.