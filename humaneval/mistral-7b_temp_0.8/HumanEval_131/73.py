
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num_arr = []
    num_str = str(n)
    for i in num_str:
        num_arr.append(int(i))
    result = 1
    for i in range(0, len(num_arr), 2):
        if num_arr[i] % 2 != 0:
            result *= num_arr[i]
    return result
