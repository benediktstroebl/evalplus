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
    
    # Create a dictionary to map word numbers to integer numbers
    word_to_int: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    words: List[str] = numbers.split()
    
    # Sort the list of words based on their integer values
    sorted_words: List[str] = sorted(words, key=lambda word: word_to_int[word])
    
    # Join the sorted list of words back into a string
    sorted_numbers: str =''.join(sorted_words)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts them in ascending order based on their integer values, and returns the sorted string. The function uses a dictionary to map word numbers to integer numbers, allowing it to sort the words correctly. The script includes a test case to demonstrate its usage.