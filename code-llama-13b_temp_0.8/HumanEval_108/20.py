
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    # 1. Check special case: empty array
    if len(arr) == 0:
        return 0
    # 2. Convert array of ints into array of strs
    arr_str = [str(num) for num in arr]
    # 3. Sum up the digits of each int and check if positive
    positive_sum = 0
    for number in arr_str:
        number_sum = 0
        for digit in number:
            number_sum += int(digit)
        if number_sum > 0:
            positive_sum += 1
    return positive_sum

