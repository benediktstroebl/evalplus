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
    # Define a dictionary to map string numbers to integer values
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
                'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}
    
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    sorted_numbers_list: List[str] = sorted(numbers_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string separated by spaces
    sorted_numbers_str: str =''.join(sorted_numbers_list)
    
    return sorted_numbers_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five nine seven'))  # Output: 'five seven nine'
print(sort_numbers('nine five one'))  # Output: 'one five nine'
```

This script defines a function `sort_numbers` that sorts a string of space-delimited numbers from 'zero' to 'nine' based on their numerical values. It uses a dictionary to map string numbers to integer values for efficient sorting. The function is then tested with several examples to demonstrate its correctness.