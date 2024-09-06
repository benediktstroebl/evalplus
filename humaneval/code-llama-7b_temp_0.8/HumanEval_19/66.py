from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Step 1: Extract the numbers from the string
    numbers_list: List[str] = numbers.split(" ")
    # Step 2: Convert the number strings to int
    numbers_list_int: List[int] = [int(num) for num in numbers_list]
    # Step 3: Sort the int list
    numbers_list_int.sort()
    # Step 4: Convert the sorted int list back to string
    numbers_list = [str(num) for num in numbers_list_int]
    # Step 5: Join the sorted string list
    return " ".join(numbers_list)

