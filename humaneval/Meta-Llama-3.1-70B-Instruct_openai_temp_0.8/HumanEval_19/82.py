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
    # Create a dictionary mapping the words to their corresponding numbers
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    num_words = numbers.split()

    # Sort the list of words based on their corresponding numbers
    sorted_words = sorted(num_words, key=lambda x: num_dict[x])

    # Join the sorted list of words back into a string
    sorted_numbers =''.join(sorted_words)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script uses a dictionary to map the word representations of numbers to their corresponding integer values. It then splits the input string into a list of words, sorts the list based on the dictionary values, and finally joins the sorted list back into a string.