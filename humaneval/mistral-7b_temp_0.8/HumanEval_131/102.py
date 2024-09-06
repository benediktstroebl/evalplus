
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    num_string = str(n)
    num_list = list(num_string)
    num_list_clean = [int(num) for num in num_list if num % 2 != 0]
    if len(num_list_clean) == 0:
        return 0
    else:
        return reduce(lambda a, b: a * b, num_list_clean)
