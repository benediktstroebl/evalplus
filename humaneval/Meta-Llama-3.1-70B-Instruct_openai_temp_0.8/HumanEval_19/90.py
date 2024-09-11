```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine' as input, 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A string of space-delimited numberals.

    Returns:
        str: A string with numbers sorted from smallest to largest.
    """

    # Define a dictionary to map number words to their corresponding integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their corresponding integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list of number words into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts them based on their corresponding integer values, and returns the sorted string. The example usage demonstrates how to use this function with the input string `'three one five'`.