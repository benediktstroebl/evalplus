
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # if num is negative
    if num < 0:
        # convert num to positive value
        num = abs(num)
        # find the sum of digits
        digits = sum(str(digit) for digit in str(num))
        # return the number of even and odd digits respectively
        return digits % 2 == 0, digits // 2 != 0
    else:
        # convert num to string
        num = str(num)
        # find the sum of digits
        digits = sum(digit * len(str(int(digit))) for digit in num)
        # return the number of even and odd digits respectively
        return digits % 2 == 0, digits // 2 != 0
