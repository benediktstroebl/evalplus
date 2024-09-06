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
    # Check if the lengths of operator and operand are compatible for the expression
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lengths must be compatible!")
    
    # Convert the operand list to a tuple to prevent modification during expression evaluation
    operand = tuple(operand)
    
    # Build and evaluate the expression
    result = functools.reduce(lambda x, y: x * y if operator[0] == '*' else
                               x + y if operator[0] == '+' else
                               x - y if operator[0] == '-' else
                               x // y if operator[0] == '//' else
                               x ** y if operator[0] == '**' else
                               x / y if y != 1 else x * y ** (1 / y)
                               , operand)
    
    return result
```

The script includes a function `do_algebra` that takes two lists as input, `operator` and `operand`. The function first checks if the lengths of `operator` and `operand` are compatible for building an expression. It then uses `funutools.reduce` to evaluate the expression using the specified rules for basic algebra operations. Finally, the function returns the result of the algebraic expression. 

Note that the script assumes that the `operand` list contains only non-negative integers, and that the `operator` list includes at least one operatory and a least two operands. Errors will be raised otherwise.