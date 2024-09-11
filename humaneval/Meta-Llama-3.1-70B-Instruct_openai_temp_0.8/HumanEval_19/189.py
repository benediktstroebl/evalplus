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
    
    # Define a mapping between the word representation and the integer value
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    word_numbers: List[str] = numbers.split()
    
    # Use the mapping to sort the list of words
    sorted_word_numbers: List[str] = sorted(word_numbers, key=lambda word: number_map[word])
    
    # Join the sorted words back into a string
    sorted_numbers: str =''.join(sorted_word_numbers)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script works by first splitting the input string into a list of words. It then uses a dictionary to map each word to its corresponding integer value. The `sorted` function is used with a lambda function as the `key` argument to sort the list of words based on their integer values. Finally, the sorted list of words is joined back into a string and returned.