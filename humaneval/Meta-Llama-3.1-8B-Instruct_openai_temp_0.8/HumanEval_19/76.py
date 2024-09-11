### Python Script to Sort Numbers in a String
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map number names to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Use a list comprehension to replace each number name with its integer value
    num_list = [num_dict[num] for num in num_list]
    
    # Sort the list of numbers
    num_list.sort()
    
    # Replace each integer value with its corresponding number name
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(n)] for n in num_list]
    
    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('zero two four'))  # Output: 'two zero four'
```
This script first defines a dictionary to map number names to their integer values. It then splits the input string into a list of numbers, replaces each number name with its integer value, sorts the list, replaces each integer value with its corresponding number name, and finally joins the sorted list of numbers back into a string. The script includes test cases to demonstrate its functionality.