```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): space-delimited string of numberals

    Returns:
        str: sorted string of numberals

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Create a dictionary to map the numbers to their integer value
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer value
    num_list.sort(key=lambda x: number_map[x])

    # Join the sorted list back into a string
    sorted_str: str =''.join(num_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
```

This script uses a dictionary to map the string numbers to their integer value, then sorts the list of numbers based on these integer values. The sorted list is then joined back into a string, which is returned as the result.