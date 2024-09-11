```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Inputs a space-delimited string of numberals from 'zero' to 'nine' and returns the string with numbers sorted from smallest to largest.
    
    Args:
    numbers (str): A string containing numberals separated by spaces.
    
    Returns:
    str: The input string with the numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Use a lambda function as the sorting key to sort the list based on the integer values of the number words
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string separated by spaces
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
```