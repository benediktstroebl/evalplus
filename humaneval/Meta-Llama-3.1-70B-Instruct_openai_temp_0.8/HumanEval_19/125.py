Here's the code for the function in a markdown code block:

```python
from typing import Dict, List

# Define a dictionary mapping number words to their integer equivalents
NUMBER_WORDS: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words from smallest to largest.

    Args:
    numbers (str): A string containing space-delimited number words.

    Returns:
    str: The input string with number words sorted from smallest to largest.
    """
    # Split the input string into a list of number words
    num_words: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer equivalents
    sorted_num_words: List[str] = sorted(num_words, key=lambda word: NUMBER_WORDS[word])
    
    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_num_words)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This code defines a dictionary `NUMBER_WORDS` to map number words to their integer equivalents. It then uses this dictionary to sort a list of number words based on their integer equivalents, before joining the sorted list back into a string. The example usage at the end demonstrates how to use the `sort_numbers` function.