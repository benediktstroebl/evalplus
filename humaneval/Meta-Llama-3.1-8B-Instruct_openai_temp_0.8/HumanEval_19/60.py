```python
from typing import List

# Define a dictionary to map string numbers to integer values
num_dict = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    :param numbers: A space-delimited string of numberals
    :return: The string with numbers sorted from smallest to largest
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string separated by spaces
    sorted_string: str =''.join(num_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('five one zero two'))  # Expected output: 'one zero two five'
```

This script first defines a dictionary `num_dict` to map string numbers to integer values. The `sort_numbers` function splits the input string into a list of numbers, sorts the list based on their integer values, and then joins the sorted list back into a string separated by spaces. The function returns this sorted string. The script includes two test cases to demonstrate the function's correctness.