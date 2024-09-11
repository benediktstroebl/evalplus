```python
from typing import Dict

# Dictionary to map string numbers to integers
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Map string numbers to integers and sort the list
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Test cases
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine zero four'))  # Output: 'zero four nine'
```

This script first defines a dictionary `num_dict` to map string numbers to integers. It then defines the `sort_numbers` function, which splits the input string into a list of numbers, maps these numbers to integers, sorts the list, and joins it back into a string. The function returns this sorted string. The test cases demonstrate how to use the `sort_numbers` function.