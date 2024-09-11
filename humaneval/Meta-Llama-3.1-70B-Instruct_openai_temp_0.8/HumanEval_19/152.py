```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The input string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a dictionary to map number strings to their corresponding integer values
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number strings
    num_list: List[str] = numbers.split()

    # Sort the list of number strings based on their corresponding integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of number strings back into a single string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```