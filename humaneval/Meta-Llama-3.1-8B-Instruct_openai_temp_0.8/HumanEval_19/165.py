```markdown
### Sorting Numbers in a String

This Python script takes a space-delimited string of numbers as input, sorts them in ascending order, and returns the sorted string.

#### Code
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Create a dictionary to map number names to their integer values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Convert the list of numbers to a list of integers using the dictionary
    num_list: List[int] = [num_dict[num] for num in num_list]
    
    # Sort the list of integers in ascending order
    num_list.sort()
    
    # Convert the list of integers back to a list of number names using the dictionary
    num_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(n)] for n in num_list]
    
    # Join the sorted list of numbers into a string separated by spaces
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one'))  # Output: 'one two three four five six seven eight nine'
```
#### Explanation

This script works by first splitting the input string into a list of numbers. It then creates a dictionary to map each number name to its corresponding integer value. The list of numbers is converted to a list of integers using this dictionary, sorted in ascending order, and then converted back to a list of number names. Finally, the sorted list of numbers is joined into a string separated by spaces and returned.

Note that this script assumes that the input string is a space-delimited string of numbers and that the numbers are valid (i.e., they exist in the dictionary). If the input string is not in the correct format or if it contains invalid numbers, the script may raise an error or produce incorrect results.