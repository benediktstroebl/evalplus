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
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    words = numbers.split()
    
    # Sort the list of words based on their integer equivalents
    sorted_words = sorted(words, key=lambda x: num_dict[x])
    
    # Join the sorted list of words back into a string
    sorted_numbers =''.join(sorted_words)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first splitting the input string into a list of words. It then sorts this list based on the integer equivalents of the words, which are obtained from the `num_dict` dictionary. Finally, it joins the sorted list of words back into a string and returns it.