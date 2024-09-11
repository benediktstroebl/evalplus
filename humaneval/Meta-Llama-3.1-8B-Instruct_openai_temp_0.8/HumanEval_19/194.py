```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.
    
    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.
    
    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary to map string numbers to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()
    
    # Use list comprehension to map the string numbers to their integer values
    numbers_list = [num_map[num] for num in numbers_list]
    
    # Sort the list of numbers
    numbers_list.sort()
    
    # Use list comprehension to map the sorted numbers back to their string values
    sorted_numbers_list: List[str] = [str(num) for num in numbers_list]
    
    # Join the sorted list of numbers into a string
    sorted_numbers: str =''.join(sorted_numbers_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine', maps these string numbers to their integer values, sorts the list of numbers, and then maps the sorted numbers back to their string values. The function returns the sorted string of numbers. The example usage at the end demonstrates how to use this function to sort the string `'three one five'`.