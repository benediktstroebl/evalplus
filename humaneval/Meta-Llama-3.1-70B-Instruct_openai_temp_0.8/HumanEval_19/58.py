```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.
    
    Args:
        numbers (str): A string containing space-delimited numberals.
    
    Returns:
        str: A string with the input numberals sorted from smallest to largest.
    """

    # Define a dictionary to map numberals to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()

    # Sort the list of numberals based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```