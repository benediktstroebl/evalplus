```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals

    Returns:
        str: The string with numbers sorted from smallest to largest
    """

    # Create a dictionary to map word numbers to their integer equivalents
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    num_list: List[str] = numbers.split()

    # Sort the list of word numbers based on their integer equivalents
    num_list.sort(key=lambda x: num_map[x])

    # Join the sorted list of word numbers back into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first maps word numbers to their integer equivalents, then uses the built-in `sort` method to sort the list of word numbers based on these integer equivalents. Finally, it joins the sorted list back into a string and returns it.