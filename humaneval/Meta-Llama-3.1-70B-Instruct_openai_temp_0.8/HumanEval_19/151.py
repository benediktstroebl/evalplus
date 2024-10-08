```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words from smallest to largest.

    Args:
        numbers (str): A string containing number words separated by spaces.

    Returns:
        str: A string containing the input number words sorted from smallest to largest.
    """
    # Create a dictionary to map number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words into a string separated by spaces
    sorted_numbers: str =''.join(sorted_list)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight two four'))  # Output: 'two four eight'
```
This script defines a function `sort_numbers` that takes a string of space-delimited number words, sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map number words to their integer values, sorts the list of number words based on these values, and joins the sorted list into a string. The script includes example usage of the function.