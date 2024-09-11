```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A string containing space-delimited numberals.

    Returns:
    str: The input string with numberals sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define a dictionary mapping numberals to their integer equivalents
    numeral_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer equivalents
    sorted_numerals = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted list back into a string
    sorted_string =''.join(sorted_numerals)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
```