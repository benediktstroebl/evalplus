```python
from typing import List

# Dictionary mapping word numbers to their integer values
NUMBER_MAPPING = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of word numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of word numbers.

    Returns:
        str: A string with the word numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of word numbers
    word_numbers: List[str] = numbers.split()

    # Use a lambda function to sort the word numbers based on their integer values
    sorted_word_numbers: List[str] = sorted(word_numbers, key=lambda x: NUMBER_MAPPING[x])

    # Join the sorted word numbers back into a string
    sorted_numbers: str =''.join(sorted_word_numbers)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```