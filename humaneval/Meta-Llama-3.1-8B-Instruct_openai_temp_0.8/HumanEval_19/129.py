```python
from typing import Dict

# Create a dictionary mapping string representations of numbers to their integer values
number_mapping: Dict[str, int] = {
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
        str: The string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use the dictionary to convert the numbers to integers and sort the list
    sorted_list: List[str] = sorted(num_list, key=lambda x: number_mapping[x])

    # Join the sorted list back into a string
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight five nine seven'))  # Output: 'five seven eight nine'
print(sort_numbers('one two three'))  # Output: 'one two three'
```