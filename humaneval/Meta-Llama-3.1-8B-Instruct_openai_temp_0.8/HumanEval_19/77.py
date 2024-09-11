### Sorting Numbers from String
```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Create a dictionary to map number names to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Convert the list of numbers to a list of integers
    num_list: List[int] = [num_dict[num] for num in num_list]

    # Sort the list of integers in ascending order
    num_list.sort()

    # Convert the sorted list of integers back to a list of number names
    sorted_num_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(x)] for x in num_list]

    # Join the sorted list of numbers into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that takes a space-delimited string of numbers, sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map number names to their integer values, allowing it to convert the input string into a list of integers that can be sorted. After sorting, it converts the list of integers back to a list of number names and joins them into a string.