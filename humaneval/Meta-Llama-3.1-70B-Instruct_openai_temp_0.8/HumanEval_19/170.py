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
    # Create a dictionary mapping words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    words: List[str] = numbers.split()

    # Sort the list based on the integer values of the words
    sorted_words: List[str] = sorted(words, key=lambda word: num_dict[word])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(sorted_words)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```