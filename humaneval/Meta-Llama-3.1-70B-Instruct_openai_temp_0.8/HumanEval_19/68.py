```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary mapping number words to their integer values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_words: List[str] = numbers.split()

    # Sort the number words based on their integer values
    sorted_number_words: List[str] = sorted(number_words, key=lambda x: number_map[x])

    # Join the sorted number words back into a string
    sorted_numbers: str =''.join(sorted_number_words)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that takes a space-delimited string of number words as input and returns the string with the numbers sorted from smallest to largest. The function uses a dictionary to map number words to their integer values and the `sorted` function with a custom sorting key to sort the number words. The sorted number words are then joined back into a string and returned.