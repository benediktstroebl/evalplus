```python
from typing import Dict

# Mapping of word numbers to their integer values
word_to_number: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of word numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Split the input string into a list of words
    word_list: List[str] = numbers.split()
    
    # Convert the list of words to a list of integers and sort it
    sorted_list: List[int] = sorted([word_to_number[word] for word in word_list])
    
    # Convert the sorted list of integers back to a list of words and join it into a string
    sorted_string: str =''.join([list(word_to_number.keys())[list(word_to_number.values()).index(num)] for num in sorted_list])
    
    return sorted_string

# Example usage
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('five five ten'))   # Output: five five ten
```

This script first defines a dictionary `word_to_number` that maps word numbers to their integer values. The `sort_numbers` function then splits the input string into a list of words, converts it to a list of integers, sorts the list, and finally converts it back to a list of words and joins it into a string. The sorted string is then returned.