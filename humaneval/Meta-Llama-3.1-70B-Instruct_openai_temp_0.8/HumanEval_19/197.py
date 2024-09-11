```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers: A string containing space-delimited numberals.

    Returns:
        A string with the numberals sorted from smallest to largest.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Define a dictionary to map numberals to their integer values
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_map[x])

    # Join the sorted numberals back into a string separated by spaces
    sorted_string: str =''.join(sorted_numerals)

    return sorted_string


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```