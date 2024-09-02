from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    nums = numbers.split()
    nums_digits = [list(map(lambda x: len(x), num)) for num in nums]
    nums_digits_list = [item for sublist in nums_digits for item in sublist]
    nums_digits_set = list(set(nums_digits_list))
    sorted_nums_digits = sorted(nums_digits_set)
    result = []
    for i in sorted_nums_digits:
        result.append([x for x in nums if len(x) == i])

    return " ".join(sorted([" ".join(x) for x in result], key=sort_key))

