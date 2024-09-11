```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list = numbers.split()
    
    # Sort the list of number words based on their integer values
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string separated by spaces
    sorted_str =''.join(sorted_list)
    
    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words, sorts them in ascending order, and returns the sorted string. The sorting is based on a dictionary `num_dict` that maps number words to their integer values. The `sorted` function is used with a lambda function as the `key` argument to sort the list of number words based on their integer values.