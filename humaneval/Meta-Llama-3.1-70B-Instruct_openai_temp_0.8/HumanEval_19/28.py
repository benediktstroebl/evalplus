```python
from typing import List

# Define a dictionary to map number words to their integer values
NUMBER_WORDS = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sort a space-delimited string of number words from smallest to largest.

    Args:
    numbers (str): A string containing number words separated by spaces.

    Returns:
    str: The input string with number words sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of number words
    number_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(number_list, key=lambda x: NUMBER_WORDS[x])

    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts the number words based on their integer values, and returns the sorted string. The `NUMBER_WORDS` dictionary is used to map number words to their corresponding integer values. The `sorted` function is used with a lambda function as the `key` argument to sort the list of number words based on their integer values.