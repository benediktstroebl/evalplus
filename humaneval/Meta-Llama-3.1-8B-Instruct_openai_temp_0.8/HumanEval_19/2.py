### Sorting Numbers from a Given String
#### Problem Statement
Given a space-delimited string of numbers from 'zero' to 'nine', return the string with numbers sorted from smallest to largest.

#### Solution
```python
from typing import Dict

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
    
    # Create a dictionary to map number strings to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list into a string and return it
    return''.join(sorted_num_list)

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts the numbers from smallest to largest, and returns the sorted string. The function uses a dictionary to map number strings to their integer values, splits the input string into a list of numbers, sorts the list based on the integer values, and joins the sorted list into a string. The example usage demonstrates the function's behavior with the input string 'three one five'.