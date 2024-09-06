
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case: if all digits are even, return 0
    if all(d % 2 == 0 for d in n):
        return 0

    # handle the case where there is a single odd digit
    if n % 2 == 1:
        return d

    # recursively compute the product of the odd digits
    odd_digits = [d % 2 == 1 for d in n]
    return (d if d in odd_digits else 0) * digits(n // 2)
