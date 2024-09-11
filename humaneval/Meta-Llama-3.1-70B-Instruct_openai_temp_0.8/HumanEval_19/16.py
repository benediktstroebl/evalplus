```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map number words to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string separated by spaces
    sorted_string: str =''.join(sorted_list)
    
    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we define a function `sort_numbers` that takes a space-delimited string of number words as input. We use a dictionary to map each number word to its integer value. We split the input string into a list of number words, sort the list based on the integer values, and then join the sorted list back into a string. The result is a string with the numbers sorted from smallest to largest.