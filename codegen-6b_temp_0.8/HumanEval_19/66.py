from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if numbers == "":
        return ""
    split_numbers = numbers.split()
    # print(split_numbers)
    lst = []
    for num in split_numbers:
        lst.append(num)

    # lsst = []
    # for i in range(len(lst)):
    #     lsst.append(int(lst[i]))
    # lsst.sort()
    # print(lsst)
    # for i in range(len(lsst)):
    #     lst[i] = str(lsst[i])

    for item in lst:
        sorted_string = numbers.replace(item, "")
        sorted_string = str(sort_numbers(sorted_string))
    return sorted_string

