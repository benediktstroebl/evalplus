```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Mapping of word numbers to their integer values
    word_to_int: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split input string into list of words
    word_list: List[str] = numbers.split()
    
    # Sort list of words based on their integer values
    sorted_word_list: List[str] = sorted(word_list, key=lambda x: word_to_int[x])
    
    # Join sorted words into a string separated by spaces
    sorted_numbers: str =''.join(sorted_word_list)
    
    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we use a dictionary to map word numbers to their integer values. We then split the input string into a list of words and sort this list based on the integer values of the words. Finally, we join the sorted list of words back into a string and return it.