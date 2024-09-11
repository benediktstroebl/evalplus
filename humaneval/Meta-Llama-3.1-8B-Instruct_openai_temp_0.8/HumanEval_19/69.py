```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map string numbers to integers
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of string numbers
    str_numbers = numbers.split()
    
    # Use list comprehension to sort the list of string numbers based on their integer values
    sorted_str_numbers = sorted(str_numbers, key=lambda x: num_map[x])
    
    # Join the sorted list of string numbers back into a single string
    sorted_numbers =''.join(sorted_str_numbers)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('four nine five two'))  # Output: 'two four five nine'
print(sort_numbers('eight seven nine six'))  # Output:'six seven eight nine'
```

In this script, the `sort_numbers` function works by first defining a dictionary `num_map` to map string numbers to integers. It then splits the input string into a list of string numbers, sorts this list based on the integer values of the numbers, and finally joins the sorted list back into a single string. The `sorted` function is used with a `key` function to sort the list based on the integer values of the numbers. The `join` function is used to concatenate the elements of the sorted list into a single string.