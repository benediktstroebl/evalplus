
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # your code here
    nums = list(str(x))
    # print(nums)
    length = len(nums)
    # print(length)
    if shift > length:
        return nums[length - shift::-1]
    else:
        return nums[-shift:] + nums[:-shift]
    # print(nums)

