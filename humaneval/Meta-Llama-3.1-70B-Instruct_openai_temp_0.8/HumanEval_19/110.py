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
    # Define a dictionary to map number words to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    num_list.sort(key=lambda x: num_map[x])
    
    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script defines a function `sort_numbers` that takes a space-delimited string of number words, sorts them based on their integer values, and returns the sorted string. The `num_map` dictionary is used to map number words to their integer values, and the `split` and `join` methods are used to split and join the string, respectively. The `sort` method is used with a lambda function as the key to sort the list of number words based on their integer values.