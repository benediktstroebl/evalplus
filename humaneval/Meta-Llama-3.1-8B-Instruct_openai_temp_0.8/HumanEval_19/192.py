```python
from typing import Dict

# Define a dictionary to map string number representations to their integer equivalents
number_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of number representations
    num_list: List[str] = numbers.split()
    
    # Use a list comprehension to create a list of integer equivalents
    num_int_list: List[int] = [number_dict[num] for num in num_list]
    
    # Sort the list of integers
    num_int_list.sort()
    
    # Use a list comprehension to create a list of sorted number representations
    sorted_num_list: List[str] = [list(number_dict.keys())[list(number_dict.values()).index(num)] for num in num_int_list]
    
    # Join the sorted list of number representations into a string
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we use a dictionary to map string number representations to their integer equivalents. We then split the input string into a list of number representations, convert them to integers, sort the list, and finally convert the sorted list of integers back to string number representations before joining them into a string.