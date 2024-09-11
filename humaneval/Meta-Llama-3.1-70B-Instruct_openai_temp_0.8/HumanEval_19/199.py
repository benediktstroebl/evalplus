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
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list = numbers.split()
    
    # Use a list comprehension to sort the number words based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted number words back into a string separated by spaces
    sorted_numbers =''.join(sorted_num_list)
    
    return sorted_numbers


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five eight two'))  # Output: 'two five eight'
print(sort_numbers('nine four seven'))  # Output: 'four seven nine'
```