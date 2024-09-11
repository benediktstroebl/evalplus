```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers into a string
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('nine five one'))
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. It uses a dictionary to map numbers to their integer values, and the `sorted` function with a `key` function to sort the list of numbers. The script also includes test cases to demonstrate the function's behavior.