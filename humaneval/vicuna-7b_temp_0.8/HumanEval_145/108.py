
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Use a dictionary to store the sum of each digit,
    # where key is the digit and value is the sum of that digit.
    digits = {digit: 0 for digit in '0123456789'}
    for num in nums:
        digits[str(num)] += num

    # Create a list of the sorted numbers
    result = []
    for digit, sum in digits.items():
        if digit not in '0':
            result.append(sum)
        else:
            result.append(digits[str(num[0])])
    result.extend(digits.values())
    return result

