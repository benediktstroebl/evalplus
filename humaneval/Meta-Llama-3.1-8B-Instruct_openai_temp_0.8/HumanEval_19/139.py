### Sorting Numbers in a String
#### Problem: Sort a string of space-delimited numbers from 'zero' to 'nine'

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Sorts a space-delimited string of numbers from 'zero' to 'nine'
    
    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'
    
    Returns:
        str: The string with numbers sorted from smallest to largest
    """
    
    # Define a dictionary to map number words to their corresponding integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    word_list: List[str] = numbers.split()
    
    # Use the dictionary to replace each word with its corresponding integer value
    int_list: List[int] = [number_map[word] for word in word_list]
    
    # Sort the list of integers in ascending order
    sorted_int_list: List[int] = sorted(int_list)
    
    # Use the dictionary to replace each integer with its corresponding word
    sorted_word_list: List[str] = [list(number_map.keys())[list(number_map.values()).index(num)] for num in sorted_int_list]
    
    # Join the sorted list of words into a string
    sorted_string: str =''.join(sorted_word_list)
    
    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('five four three two one zero'))  # Output: 'zero one two three four five'
```