```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string containing space-separated numberals.

    Returns:
        str: A string with the numberals sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Define a dictionary to map numberals to their integer values
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=numeral_map.get)

    # Join the sorted list back into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-separated numberals as input, sorts them in ascending order, and returns the sorted string. The function uses a dictionary to map numberals to their integer values and the built-in `sorted` function to sort the list of numberals based on these values.