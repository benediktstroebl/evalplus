
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

    # Keep the two integers as strings
    a_str = str(a)
    b_str = str(b)

    # Convert the two integers as list of integers
    a_list = []
    b_list = []
    for number in a_str:
        a_list.append(int(number))
    for number in b_str:
        b_list.append(int(number))

    # Create the product
    product = 0
    for index in range(0, len(a_list)):
        product += a_list[index] * b_list[index]

    return product


