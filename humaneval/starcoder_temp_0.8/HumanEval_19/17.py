from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # 1: Create a list of strings from the input string.
    str_list = numbers.split()

    # 2: Create an empty list to store the sorted list of numbers
    sorted_str_list = []

    # 3: Iterate over the list of strings
    for i in range(len(str_list)):
        # 4: Append the string from the list in to the new list
        #    If the string is 'one' then append '1' instead of 'one'
        if str_list[i] == "one":
            sorted_str_list.append("1")
        else:
            sorted_str_list.append(str_list[i])

    # 5: Sort the new list of strings in place
    sorted_str_list.sort()

    # 6: Convert the list of strings back to a single string and return it
    return " ".join(sorted_str_list)

