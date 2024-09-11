```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numberals from 'zero' to 'nine' in ascending order.
    
    Args:
        numbers (str): A string containing numberals separated by spaces.
    
    Returns:
        str: The input string with numberals sorted in ascending order.
    """

    # Create a dictionary to map numberals to their corresponding integer values
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their corresponding integer values
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted list of numberals back into a string separated by spaces
    sorted_string: str =''.join(sorted_numerals)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numberals as input, sorts them in ascending order, and returns the sorted string. The sorting is done using a dictionary to map numberals to their corresponding integer values, which allows the use of Python's built-in `sorted` function with a custom sorting key.