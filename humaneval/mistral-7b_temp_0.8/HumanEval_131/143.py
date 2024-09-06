
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # your code here
    n1 = int(n)
    if n1 == 0:
        return 0
    else:
        n2 = []
        while n1 > 0:
            n3 = n1 % 10
            if n3 % 2 == 1:
                n2.append(n3)
            n1 = int(n1 / 10)
        return int(n2[0]) * int(n2[1]) * int(n2[2])
