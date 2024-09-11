```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numerals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string containing space-delimited numerals.

    Returns:
        str: The input string with numerals sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Define a dictionary to map numerals to their integer values
    numeral_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numerals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numerals based on their integer values
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_mapping[x])

    # Join the sorted list of numerals back into a string
    sorted_string: str =''.join(sorted_numerals)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```