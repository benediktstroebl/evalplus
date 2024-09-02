
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0

    # If the number is negative
    if num < 0:
        # First make the number positive
        num = num * (-1)

    # If the number is 0
    if num == 0:
        # Even count is 1
        even += 1
    else:
        # While there are more than 0 digits in num
        while num > 0:
            # Get the last digit
            digit = num % 10
            # If the digit is 0 or 2, 4, 6, 8
            if digit % 2 == 0:
                # Even count is incremented by 1
                even += 1
            else:
                # Otherwise, odd count is incremented by 1
                odd += 1
            # Delete the last digit
            num = num // 10

    return even, odd

