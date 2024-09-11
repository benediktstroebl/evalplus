```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Create a dictionary to map word numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of word numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of word numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of word numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```