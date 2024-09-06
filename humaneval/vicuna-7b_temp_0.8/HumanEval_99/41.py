
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # Get the digits of the number as a list
    digits = [int(digit) for digit in str(value)]

    # Find the largest digit
    max_digit = max(digits)

    # Get the sign of the number
    sign = value < 0

    # If the largest digit is positive, the number is negative
    if max_digit > 0:
        value = -value

    # If the largest digit is negative, the number is positive
    elif max_digit < 0:
        max_digit = -max_digit

    # If the largest digit is zero, the number is positive or negative
    # depending on the sign of the number
    elif max_digit == 0:
        max_digit = sign

    # If the largest digit is negative and the number is positive
    # the number is rounded away from zero
    elif max_digit < 0:
        max_digit = -max_digit

    # Create a list of integers
    nums = []

    # Create the number of integers after the largest digit
    for i in range(max_digit + 1):
        if digits[i] == max_digit:
            nums.append(max_digit)
            break
        else:
            nums.append(i)

    # Create the closest integer to the value
    closest_digit = nums[0]

    # Loop through the list of integers and adjust the closest digit as necessary
    for digit in nums:
        if abs(digits[digit]) > abs(digits[nums[nums.index(closest_digit) + digit - 1]]):
            if digits[digit] > 0:
                closest_digit = digit + 1
            elif digits[digit] < 0:
                closest_digit = digit - 1

    return closest_digit