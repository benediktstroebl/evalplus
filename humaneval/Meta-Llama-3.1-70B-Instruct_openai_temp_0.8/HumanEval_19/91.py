```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map word numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    words = numbers.split()
    
    # Sort the list of words based on their integer equivalents
    sorted_words = sorted(words, key=lambda x: num_map[x])
    
    # Join the sorted list of words into a single string
    sorted_numbers =''.join(sorted_words)
    
    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```