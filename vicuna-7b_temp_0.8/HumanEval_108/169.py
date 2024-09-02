
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
    # Use a dictionary to count the number of positive and negative numbers
    # with certain digits in the first three places.
    # For example, to count the number of positive 11s, we need to include
    # the numbers 11 and -11, but exclude the number -1.
    num_count = {
        '1': 0,
        '2': 0,
        '11': 0,
        '-1': 0,
        '-2': 0,
        '-11': 0,
        '11': 0,
        '12': 0,
        '21': 0,
        '111': 0,
        '-11': 0,
        '112': 0,
        '121': 0,
        '211': 0,
        '122': 0,
        '221': 0,
        '1111': 0,
        '-111': 0,
        '1112': 0,
        '1121': 0,
        '1211': 0,
        '1212': 0,
        '2111': 0,
        '2112': 0,
        '2121': 0,
        '2211': 0,
        '2212': 0,
        '2221': 0,
        '11111': 0,
        '-1111': 0,
        '11112': 0,
        '11121': 0,
        '11211': 0,
        '11212': 0,
        '12111': 0,
        '12112': 0,
        '12121': 0,
        '12211': 0,
        '12212': 0,
        '12221': 0,
        '12222': 0,
        '111
