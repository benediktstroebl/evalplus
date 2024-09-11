```python
from typing import Dict, List

# Define a dictionary that maps number words to their integer values
NUMBER_MAPPING: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of number words
    number_words: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    sorted_number_words: List[str] = sorted(number_words, key=NUMBER_MAPPING.get)
    
    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_number_words)
    
    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight four six two'))  # Output: 'two four six eight'
```
This script uses a dictionary to map number words to their integer values. The `sort_numbers` function splits the input string into a list of number words, sorts the list based on the integer values, and then joins the sorted list back into a string. The `NUMBER_MAPPING` dictionary is used as the sorting key to ensure that the number words are sorted correctly.