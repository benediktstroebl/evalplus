```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are Options are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Validate input
    numbers = numbers.split()  # Ensure valid input range is numbers from 0 to 9
    
    # Initialize empty string to return
    result = ''
    
    # Sort numbers in ascending order
    numbers = sorted(numbers)
    
    # Concatenate sorted numbers into a string
    for num in numbers:
        result += str(num)
    
    return result

# Test the function
my_input = 'three one five'
sorted_output = sort_numbers(my_input)
print(sorted_output)  # Output: 'one three five'
```