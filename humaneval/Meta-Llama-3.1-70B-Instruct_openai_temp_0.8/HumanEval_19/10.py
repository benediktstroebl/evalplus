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
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of number words as input, sorts them in ascending order, and returns the sorted string. The sorting is based on a dictionary `num_map` that maps each number word to its corresponding integer value. The `sorted` function is used with a lambda function as the `key` argument to sort the list of number words based on their integer values.