
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        raise ValueError('Input n should be a positive integer')
    elif n == 0:
        return 0
    else:
        # We can use list comprehension
        digits_n = [int(i) for i in str(n)]
        odd_digits = []
        for i in digits_n:
            if i % 2 == 1:
                odd_digits.append(i)
            else:
                continue
        return 0 if odd_digits == [] else product(odd_digits)
