
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
    # convert input list of integers to list of digits
    digits = [int(n) for n in nums]
    while digits:
        # get the last digit from the list
        digit = digits.pop()
        # check if the last digit is positive
        if digit > 0:
            # add the digit to the result list
            result = [digit] + result
        else:
            # if the last digit is negative, we check if the next
            # digit is more negative than the last digit
            next_digit = digits[0]
            if next_digit < 0:
                result = [-next_digit] + result
            else:
                # if the next digit is less negative than the last digit
                # or if the last digit is zero, we add the digit to the result list
                result = [digit] + result
        # add the next digit to the list
        digits.append(0)
    return result