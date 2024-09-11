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
    
    # Define a dictionary to map word numbers to their integer equivalents
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    words: List[str] = numbers.split()
    
    # Sort the list of words based on their integer equivalents
    sorted_words: List[str] = sorted(words, key=lambda word: num_dict[word])
    
    # Join the sorted list of words back into a string
    sorted_string: str =''.join(sorted_words)
    
    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```