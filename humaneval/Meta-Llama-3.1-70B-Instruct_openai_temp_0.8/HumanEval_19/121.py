```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A string containing space-delimited numberals.

    Returns:
    str: The input string with numberals sorted from smallest to largest.
    """
    # Define a dictionary to map numberals to their corresponding integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()

    # Sort the list of numberals based on their corresponding integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of numberals back into a string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  
# Output: 'zero one two three four five six seven eight nine'
```