

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # using deque to optimize popping from the left
    nums = deque([int(x) for x in str(number)])
    if not nums:
        return 0

    if nums[0] == 0 and len(nums) > 1:
        return float(''.join(str(num) for num in nums))

    return float(''.join(str(num) for num in nums))

