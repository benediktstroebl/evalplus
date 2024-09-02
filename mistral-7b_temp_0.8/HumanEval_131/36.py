
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    new_n = str(n)
    even = 0
    odd = 1
    for i in new_n:
        if i.isdigit():
            if int(i) % 2 == 0:
                even += int(i)
            else:
                odd *= int(i)

    if even == 0:
        return odd
    else:
        return even
