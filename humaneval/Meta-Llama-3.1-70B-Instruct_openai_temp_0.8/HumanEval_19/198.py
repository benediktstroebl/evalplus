```python
from typing import List, Dict

# Define a dictionary mapping number words to their corresponding integer values
NUMBER_MAPPING: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words in ascending order.

    Args:
        numbers (str): A string containing space-delimited number words.

    Returns:
        str: The input string with the number words sorted from smallest to largest.

    Raises:
        ValueError: If the input string contains invalid number words.
    """

    # Split the input string into a list of number words
    number_words: List[str] = numbers.split()

    # Validate the input number words and map them to their corresponding integer values
    try:
        number_values: List[int] = [NUMBER_MAPPING[word] for word in number_words]
    except KeyError as e:
        raise ValueError(f"Invalid number word: {e}")

    # Sort the list of integer values
    sorted_values: List[int] = sorted(number_values)

    # Map the sorted integer values back to their corresponding number words
    sorted_words: List[str] = [word for value, word in sorted((value, word) for value, word in NUMBER_MAPPING.items() if value in sorted_values)]

    # Join the sorted number words back into a string
    sorted_numbers: str =''.join(sorted_words)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts them in ascending order, and returns the sorted string. The function uses a dictionary `NUMBER_MAPPING` to map number words to their corresponding integer values, allowing it to sort the number words based on their integer values. The script also includes a test case to demonstrate the function's usage.