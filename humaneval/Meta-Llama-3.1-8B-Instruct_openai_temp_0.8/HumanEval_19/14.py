```python
from typing import Dict

# Define a dictionary to map string numbers to integers
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3,
    'four': 4, 'five': 5,'six': 6,'seven': 7,
    'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we first define a dictionary `num_dict` to map string numbers to integers. Then we define the `sort_numbers` function, which takes a space-delimited string of numbers as input, splits it into a list, sorts the list using the dictionary as a key, and then joins the sorted list back into a string. The function returns this sorted string. Finally, we provide an example usage of the function.