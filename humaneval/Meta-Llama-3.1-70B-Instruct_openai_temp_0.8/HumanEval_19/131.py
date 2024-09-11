```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Dictionary mapping word numbers to their integer equivalents
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    num_list: List[str] = numbers.split()

    # Sort the list of word numbers based on their integer equivalents
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that sorts a space-delimited string of word numbers from 'zero' to 'nine' in ascending order. It uses a dictionary to map word numbers to their integer equivalents, which allows it to sort the numbers correctly. The sorted numbers are then joined back into a string and returned.