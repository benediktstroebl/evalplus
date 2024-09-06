
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = str(n)
    num_list = list(num)
    num_list_odd = []
    for i in range(len(num_list)):
        if int(num_list[i]) % 2 != 0:
            num_list_odd.append(int(num_list[i]))
    prod = 1
    for i in num_list_odd:
        prod *= i
    return prod

