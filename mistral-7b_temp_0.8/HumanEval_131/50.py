
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    for i in range(len(n)):
        if n[i] % 2 != 0:
            print(n[i])
            return int(n[i]) * int(n[i+1]) * int(n[i+2])
        else:
            continue
    else:
        return 0
