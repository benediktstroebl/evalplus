
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Inserts 0 at beginning if shift is greater than number of digits
    zero = 0 if shift > len(str(x)) else 1

    # Splits the number into a list of strings
    nums = list(str(x))
    nums = nums[zero:] + nums[:zero]

    # Shifts the list
    if shift > 0:
        nums = nums[:-shift]
    else:
        nums = nums[shift:] + nums[:shift]

    # Joins the list with character
    nums = "".join(nums)

    # Returns the result
    return nums

