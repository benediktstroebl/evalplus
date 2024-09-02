
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # check if number is negative
    if num < 0:
        return (abs(num)//2, abs(num)%2)
    # check if number is 0
    elif num == 0:
        return (0, 0)
    # check if number is 1
    elif num == 1:
        return (0, 1)
    # check if number is 2
    elif num == 2:
        return (1, 0)
    # split number into digits
    digits = []
    for i in range(len(str(num))):
        digits.append(str(num)[i])
    # check if the number is a multiple of 4
    if sum(map(len, digits)) % 4 == 0:
        # number has an even number of digits
        even_count = sum(map(lambda x: x//2 if x % 2 == 0 else x, digits))
        # check if the last digit is even
        last_digit = digits[-1]
        if last_digit % 2 == 0:
            odd_count = 1
        else:
            odd_count = 0
    else:
        # number has an odd number of digits
        even_count = 0
        odd_count = sum(map(lambda x: x//2 if x % 2 == 0 else x, digits))
    # return the number of even and odd digits
    return (even_count, odd_count)
