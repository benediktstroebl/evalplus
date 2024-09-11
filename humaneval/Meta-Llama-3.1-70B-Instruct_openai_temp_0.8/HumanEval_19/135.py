```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map number words to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_words = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_number_words = sorted(number_words, key=lambda x: number_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_number_words)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines the `sort_numbers` function, which takes a space-delimited string of number words, sorts them in ascending order, and returns the sorted string. It uses a dictionary to map number words to their integer values, allowing it to sort the words correctly. The script also includes a test case to demonstrate the function's usage.