```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A string containing number words separated by spaces.

    Returns:
    str: A string with the number words sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a dictionary to map number words to their corresponding numerical values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their corresponding numerical values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts them in ascending order based on their corresponding numerical values, and returns the sorted string. The function uses a dictionary to map number words to their numerical values and the built-in `sorted` function with a custom sorting key to sort the list of number words.