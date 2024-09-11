```python
from typing import List

# Define a dictionary that maps number words to their corresponding numerical values
number_mapping = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of number words
    number_words = numbers.split()
    
    # Sort the list of number words based on their corresponding numerical values
    sorted_number_words = sorted(number_words, key=lambda x: number_mapping[x])
    
    # Join the sorted list of number words back into a string separated by spaces
    sorted_numbers =''.join(sorted_number_words)
    
    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```