```python
from typing import List

# Define a dictionary to map number words to their integer equivalents
num_to_word = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words from smallest to largest.

    Args:
    numbers (str): A string containing space-delimited number words.

    Returns:
    str: The input string with the number words sorted from smallest to largest.
    """
    # Split the input string into a list of number words
    words = numbers.split()

    # Use the dictionary to map number words to their integer equivalents, sort, and map back to words
    sorted_numbers = sorted(words, key=lambda x: num_to_word[x])

    # Join the sorted number words back into a string
    sorted_string =''.join(sorted_numbers)

    return sorted_string


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```