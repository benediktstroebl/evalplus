
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    digits = list(map(int, str(n)))
    evens = []
    odds = []
    for digit in digits:
        if digit % 2 == 0:
            evens.append(digit)
        else:
            odds.append(digit)
    product_of_odds = 1
    for i in range(0, len(odds)):
        product_of_odds = product_of_odds * odds[i]
    return product_of_odds
