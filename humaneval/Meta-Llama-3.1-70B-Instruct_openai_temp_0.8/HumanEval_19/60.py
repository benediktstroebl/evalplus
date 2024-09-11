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
    # Create a dictionary to map the word representation of numbers to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    num_list: List[str] = numbers.split()

    # Use the dictionary to convert the word representation to integer values, sort, and then convert back to words
    sorted_nums = [word for _, word in sorted(zip([num_map[num] for num in num_list], num_list))]

    # Join the sorted list of words back into a string separated by spaces
    sorted_nums_str =''.join(sorted_nums)

    return sorted_nums_str


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```