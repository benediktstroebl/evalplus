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
    
    # Define the mapping of word numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    word_numbers: List[str] = numbers.split()

    # Sort the list of word numbers based on their integer equivalents
    sorted_word_numbers = sorted(word_numbers, key=lambda x: num_map[x])

    # Join the sorted list of word numbers into a string
    sorted_numbers =''.join(sorted_word_numbers)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight two six four'))  # Output: 'two four six eight'
```

This script defines a function `sort_numbers` that sorts a space-delimited string of word numbers from smallest to largest. It uses a dictionary to map word numbers to their integer equivalents and the built-in `sorted` function with a custom sorting key to sort the list of word numbers. The sorted list is then joined back into a string and returned as the result.