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
    
    # Define a dictionary to map number words to their integer values
    number_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    number_words: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    sorted_words: List[str] = sorted(number_words, key=lambda x: number_dict[x])
    
    # Join the sorted list of number words back into a string
    sorted_string: str =''.join(sorted_words)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```