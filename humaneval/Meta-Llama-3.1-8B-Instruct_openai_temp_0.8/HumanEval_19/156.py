### Sorting Numbers in a String
#### Problem Description
The `sort_numbers` function takes a string of space-delimited numbers from 'zero' to 'nine', sorts them in ascending order, and returns the sorted string.

#### Solution
```python
from typing import Dict
from collections import Counter

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The sorted string of numbers.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Define a dictionary to map string numbers to their integer equivalents
    num_mapping: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Count the occurrences of each number in the input string
    num_counts: Counter = Counter(numbers.split())

    # Sort the numbers based on their integer values
    sorted_nums: List[str] = sorted(num_counts, key=lambda x: num_mapping[x])

    # Join the sorted numbers back into a string
    sorted_string: str =''.join(sorted_nums)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight five zero'))  # Output: 'zero five eight'
```
This solution uses a dictionary to map string numbers to their integer equivalents, a counter to count the occurrences of each number, and the built-in `sorted` function with a custom key function to sort the numbers. The sorted numbers are then joined back into a string.