### Sorting Numbers in a String
#### Problem Statement
Input is a space-delimited string of numberals from 'zero' to 'nine'. 
Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'. 
Return the string with numbers sorted from smallest to largest

#### Solution
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Define a dictionary mapping number strings to their integer values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five nine four seven three'))  # Output: 'three four five seven nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map number strings to their integer values, allowing for efficient sorting.