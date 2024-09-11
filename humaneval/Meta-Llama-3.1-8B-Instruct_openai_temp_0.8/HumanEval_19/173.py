```markdown
**Sorted Numbers Function**
=====================================

A Python function to sort space-delimited numbers from 'zero' to 'nine' in ascending order.

```python
from typing import List

# Dictionary mapping number words to their integer values
num_dict = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('seven eight nine'))  # Output:'seven eight nine'
print(sort_numbers('five four three two one'))  # Output: 'one two three four five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of number words as input, sorts them in ascending order based on their integer values, and returns the sorted string. The `num_dict` dictionary is used to map number words to their integer values. The `sorted` function is used to sort the list of number words, and the `join` function is used to join the sorted list back into a string.