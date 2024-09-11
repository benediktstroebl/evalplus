```python
from typing import Tuple


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numbers

    Returns:
    str: The input string with numbers sorted from smallest to largest

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of numbers
    num_list: List[Tuple[int, str]] = [(i, num) for i, num in enumerate(numbers.split())]

    # Sort the list based on the numeric value of each number
    num_list.sort(key=lambda x: num_to_int(x[1]))

    # Join the sorted list into a string
    sorted_numbers =''.join([num[1] for num in num_list])

    return sorted_numbers


def num_to_int(num: str) -> int:
    """
    Convert a number string to its corresponding integer value

    Args:
    num (str): A number string from 'zero' to 'nine'

    Returns:
    int: The integer value of the input number

    Example:
    >>> num_to_int('three')
    3
    """

    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    return num_map[num]


if __name__ == "__main__":
    # Test the function
    print(sort_numbers('three one five'))
```

This script defines a function `sort_numbers` that sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order. The `num_to_int` function is used to convert each number string to its corresponding integer value, which is then used for sorting. The script includes example usage and a test case at the end.