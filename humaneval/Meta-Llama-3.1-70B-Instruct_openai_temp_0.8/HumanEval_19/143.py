```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The input string with numbers sorted from smallest to largest.

    Raises:
    ValueError: If the input string contains an invalid number word.
    """

    # Map number words to their corresponding integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_words = numbers.split()

    # Check if all number words are valid
    if not all(word in num_map for word in num_words):
        raise ValueError("Invalid number word in the input string")

    # Sort the number words based on their corresponding integer values
    sorted_num_words = sorted(num_words, key=lambda word: num_map[word])

    # Join the sorted number words back into a string
    sorted_numbers =''.join(sorted_num_words)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```