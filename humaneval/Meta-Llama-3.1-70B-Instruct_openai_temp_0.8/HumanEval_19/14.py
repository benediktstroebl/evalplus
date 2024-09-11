```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numberals from 'zero' to 'nine' in ascending order.
    
    Args:
    numbers (str): A string of space-delimited numberals.
    
    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts them in ascending order based on their integer values, and returns the sorted string. The function uses a dictionary to map number words to their integer values and the built-in `sorted` function with a custom sorting key to sort the list of number words.