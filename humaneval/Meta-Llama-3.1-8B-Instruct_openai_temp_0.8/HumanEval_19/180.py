```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map number names to their integer values
    num_dict: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('nine eight seven'))
```

This Python script defines a function `sort_numbers` that takes a string of space-delimited number names, maps them to their integer values, sorts the numbers based on these values, and returns the sorted string. The function uses a dictionary to map number names to their integer values and the built-in `sorted` function with a lambda function as the `key` argument to sort the numbers.