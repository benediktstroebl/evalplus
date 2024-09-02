
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
    # YOUR CODE HERE

    # The dictionary to store the first digit
    def get_dic(num):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str(num)[0]]

    # The dictionary to store the other digit
    def get_dic_omit_last(num):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[num[:-1]]

    # add the second digit to the first digit
    def add_dic(a, b):
        return a * 10 + b

    # return the result
    return get_dic(str(a) + '0' + str(b))

