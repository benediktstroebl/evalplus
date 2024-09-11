```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numbers

    Returns:
    str: The string with numbers sorted from smallest to largest
    """

    # Create a dictionary to map string numbers to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    nums = numbers.split()

    # Convert the list of numbers from string to integer using the num_map dictionary
    nums = [num_map[num] for num in nums]

    # Sort the list of numbers in ascending order
    nums.sort()

    # Convert the sorted list of numbers back to string using the num_map dictionary
    nums = [sorted_num_map[num] for num in nums]

    # Join the sorted list of numbers back into a string separated by spaces
    sorted_numbers =''.join(nums)

    return sorted_numbers


# Example usage:
sorted_numbers = sort_numbers('three one five')
print(sorted_numbers)  # Output: 'one three five'

```