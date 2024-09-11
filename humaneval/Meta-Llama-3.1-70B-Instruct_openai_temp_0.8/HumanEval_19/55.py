```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine',
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A string containing space-delimited numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map number words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list = numbers.split()

    # Use the dictionary to convert number words to integers, sort them, and then convert back to words
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted number words back into a string separated by spaces
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  
# Output: 'zero one two three four five six seven eight nine'
print(sort_numbers('five four three two one'))  
# Output: 'one two three four five'
print(sort_numbers('zero nine eight seven six five four three two one'))  
# Output: 'zero one two three four five six seven eight nine'
```