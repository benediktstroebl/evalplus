
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    if x == "1/1" or n == "1/1":
        return True
    if x == "0/1" or n == "0/1":
        return True

    first_int = 0
    second_int = 0
    first_int_str = ""
    second_int_str = ""

    for char in x:
        if char.isdigit():
            first_int_str += char
        elif char == "/":
            break
    first_int = int(first_int_str)

    for char in n:
        if char.isdigit():
            second_int_str += char
        elif char == "/":
            break
    second_int = int(second_int_str)

    return first_int / second_int == int(first_int / second_int)

