
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
    if len(operator)!= len(operand) - 1:
        raise ValueError("Operator list must have one less element than operand list")

    if len(operator) == 0 or len(operand) == 0:
        raise ValueError("Operator and operand list must not be empty")

    if len(operator) < 1:
        raise ValueError("Operator list must have at least one element")

    if len(operand) < 2:
        raise ValueError("Operand list must have at least two element")

    if not all(isinstance(item, int) for item in operand):
        raise TypeError("All items in operand list must be integer")

    if not all(item in ["+", "-", "*", "//", "**"] for item in operator):
        raise ValueError("Operator list can only have operators: +, -, * or **")

    if not all(operand[i] >= 0 for i in range(len(operand))):
        raise ValueError("All elements in operand list must be non-negative")

    algebra_operator_dict = {
        "+": operator.count("+"),
        "-": operator.count("-"),
        "*": operator.count("*"),
        "//": operator.count("//"),
        "**": operator.count("**"),
    }

    if algebra_operator_dict["//"] > 0 and any(
        operand[i] % operand[i + 1]!= 0 for i in range(len(operand) - 1)
    ):
        raise ValueError("Invalid operands for '//' operator")

    if algebra_operator_dict["**"] > 0 and any(operand[i] < 0 for i in range(len(operand))):
        raise ValueError("Invalid operand for '**' operator")

    if any(operand[i + 1] == 0 and operand[i + 2] in ["//", "**"] for i in range(len(operand) - 2)):
        raise ValueError("Zero division or zero power is not defined")

    for i in range(len(operand)):
        if operand[i] > 0 and operand[i + 1] in ["+", "-", "*", "//", "**"]:
            raise ValueError(
                "Only the first operand can be positive number for algebra expression"
            )

    algebra_expression = "".join([str(item) for item in operand])
    algebra_expression = algebra_expression.replace("//", "/")
    algebra_expression = algebra_
