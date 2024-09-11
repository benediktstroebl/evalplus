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
    
    # Define a dictionary to map numeral words to their integer values
    numeral_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numeral words
    numeral_words = numbers.split()
    
    # Convert the numeral words to their integer values, sort them, and map them back to numeral words
    sorted_numerals = [numeral for _, numeral in sorted((numeral_map[word], word) for word in numeral_words)]
    
    # Join the sorted numeral words into a space-delimited string
    sorted_numbers =''.join(sorted_numerals)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```