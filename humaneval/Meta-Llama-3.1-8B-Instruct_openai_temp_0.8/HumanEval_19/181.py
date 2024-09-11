### Number Sorter
#### Self-Contained Python Script
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
    """
    # Define a dictionary to map string numbers to integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list of numbers back into a string
    sorted_str: str =''.join(sorted_num_list)

    return sorted_str


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four two'))   # Output: 'two four nine'
```
This script defines a `sort_numbers` function that takes a space-delimited string of numbers as input and returns the sorted string. The function uses a dictionary to map string numbers to integer values, splits the input string into a list of numbers, sorts the list based on the integer values, and then joins the sorted list back into a string. The example usage demonstrates the function's behavior with two different inputs.