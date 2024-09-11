```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()
    
    # Define a dictionary to map number strings to their corresponding integer values
    number_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Use a custom sorting key to sort the list based on the integer values
    sorted_numbers_list: List[str] = sorted(numbers_list, key=lambda x: number_map[x])
    
    # Join the sorted list back into a string with spaces in between
    sorted_numbers_string: str =''.join(sorted_numbers_list)
    
    return sorted_numbers_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one'))  # Output: 'one two three four five six seven eight nine'
```

In this script, the `sort_numbers` function takes a space-delimited string of numbers as input, splits it into a list, sorts the list based on the integer values of the numbers, and then joins the sorted list back into a string with spaces in between. The `sorted` function is used with a custom sorting key to achieve this.