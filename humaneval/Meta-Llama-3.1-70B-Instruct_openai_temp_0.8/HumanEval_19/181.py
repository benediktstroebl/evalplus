```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited number words from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A string containing number words separated by spaces.

    Returns:
    str: The input string with the number words sorted in ascending order.

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a dictionary mapping number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list back into a string separated by spaces
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```