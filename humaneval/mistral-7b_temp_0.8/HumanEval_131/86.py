
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # TODO: Write your solution below!

    temp = []
    if n == 0:
        return 0
    else:
        while n != 0:
            if n % 10 % 2 != 0:
                temp.append(n % 10)
            n //= 10
        if len(temp) == 0:
            return 0
        else:
            return reduce(lambda x, y: x * y, temp)

