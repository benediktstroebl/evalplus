### Sorting Numbers in a String
#### Python Script
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
    """
    # Define a dictionary to map string numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))
# Output: one three five
```
This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them based on their integer values, and returns the sorted string. The example usage demonstrates how to use this function with the input `'three one five'`.