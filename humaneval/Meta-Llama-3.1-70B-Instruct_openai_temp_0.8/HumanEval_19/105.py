```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define a dictionary to map number words to their corresponding integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_words = numbers.split()

    # Sort the list of number words based on their corresponding integer values
    sorted_num_words = sorted(num_words, key=lambda word: num_map[word])

    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_words)

    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```