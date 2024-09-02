
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    
    assert type(a) == int and type(b) == int, "a and b should be integers."

    list_a = list(map(int, str(abs(a))))
    list_b = list(map(int, str(abs(b))))

    list_product = [a * b for a, b in zip(list_a, list_b)]
    result = 0

    for digit in list_product:
        result += digit

    return result
