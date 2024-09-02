
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # your code here
    # 1. get all odd digit numbers
    # 2. get all even digit numbers
    # 3. get odd digit numbers - even digit numbers = unique digits

    # step 1
    odd_digit_nums = []
    for num in x:
        if not has_even_digit(num):
            odd_digit_nums.append(num)

    # step 2
    even_digit_nums = []
    for num in x:
        if has_even_digit(num):
            even_digit_nums.append(num)

    # step 3
    uniques = odd_digit_nums[:]
    for num in odd_digit_nums:
        if num in even_digit_nums:
            uniques.remove(num)

    return sorted(uniques)

