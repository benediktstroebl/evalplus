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
    
    # Define a dictionary to map number words to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Sort the list based on the integer equivalents of the number words
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list back into a string separated by spaces
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```