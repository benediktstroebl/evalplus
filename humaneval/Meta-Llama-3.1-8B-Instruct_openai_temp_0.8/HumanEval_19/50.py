```python
from typing import Dict

# Dictionary to map numeral strings to their corresponding integer values
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numeral strings

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numeral strings
    num_list: list[str] = numbers.split()

    # Use the dictionary to map each numeral string to its corresponding integer value
    num_list: list[int] = [num_dict[num] for num in num_list]

    # Sort the list of integer values in ascending order
    num_list.sort()

    # Map the sorted integer values back to their corresponding numeral strings
    sorted_nums: list[str] = [list(num_dict.keys())[list(num_dict.values()).index(n)] for n in num_list]

    # Join the sorted list of numeral strings into a single string with spaces in between
    sorted_numbers: str =''.join(sorted_nums)

    return sorted_numbers

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine zero one'))  # Output: 'zero one nine'
```
This script first creates a dictionary to map each numeral string to its corresponding integer value. It then splits the input string into a list of numeral strings, maps each numeral string to its integer value, sorts the list of integer values, and finally maps the sorted integer values back to their corresponding numeral strings.