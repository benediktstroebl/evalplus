Here's a Python script that solves the problem.

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numberals

    Returns:
    str: The string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary to map number strings to integers
    num_dict: dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Use list comprehension to sort the list of numbers
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string
    sorted_str: str =''.join(sorted_num_list)

    return sorted_str

numbers: str = input("Enter a space-delimited string of numbers (zero to nine): ")
print(sort_numbers(numbers))
```

This script defines a function `sort_numbers` that sorts a space-delimited string of numberals from 'zero' to 'nine' and returns the string with numbers sorted from smallest to largest. It uses a dictionary to map number strings to integers for sorting. The script then takes a string input from the user and prints the sorted string.