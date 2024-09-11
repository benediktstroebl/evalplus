```python
# Solution to the problem of sorting numbers from a string

from typing import Dict, List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map string representations to numerical values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their numerical values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string and return the result
    return''.join(sorted_list)

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers, sorts them based on their numerical values, and returns the sorted string. The sorting is done using the `sorted` function with a custom key function that looks up the numerical value of each number in the input string using a dictionary. The sorted list is then joined back into a string using the `join` method, and the result is returned.