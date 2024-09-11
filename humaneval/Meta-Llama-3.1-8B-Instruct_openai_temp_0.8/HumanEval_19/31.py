```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Define a dictionary to map string numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of strings
    num_list: List[str] = numbers.split()

    # Remove the ordinal suffix from each number and sort the list
    sorted_list: List[str] = sorted([num[:-2] if num.endswith(('st', 'nd', 'rd')) else num for num in num_list])

    # Map the sorted list back to string numbers and join it back into a string
    sorted_numbers: str =''.join([num_dict[num] for num in sorted_list])

    # Replace integer values with string numbers
    sorted_numbers: str =''.join([num_dict[num] for num in sorted_numbers.split()])

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('eight nine zero'))
print(sort_numbers('seven five one'))
```

This script will first split the input string into a list of numbers, remove the ordinal suffix from each number (if any), sort the list, map the sorted list back to string numbers, and finally join the sorted list back into a string. Note that this script assumes that the input string contains only valid numbers.