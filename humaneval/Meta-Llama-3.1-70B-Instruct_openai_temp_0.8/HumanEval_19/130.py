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
    # Create a dictionary to map word numbers to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    words = numbers.split()

    # Sort the list of words based on their corresponding integer values
    sorted_words = sorted(words, key=lambda word: num_map[word])

    # Join the sorted list of words back into a string
    sorted_string =''.join(sorted_words)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

You can run this script as is. It defines the `sort_numbers` function as per your requirements and includes an example usage at the end.