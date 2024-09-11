```python
from typing import List, Dict

# Dictionary to map string representations of numbers to their integer values
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
   'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of words (numbers)
    num_list: List[str] = numbers.split()
    
    # Use a list comprehension to create a list of tuples, where each tuple contains a word and its corresponding integer value
    num_list_sorted: List[tuple] = [(word, num_dict[word]) for word in num_list]
    
    # Sort the list of tuples based on the integer value
    num_list_sorted.sort(key=lambda x: x[1])
    
    # Use a list comprehension to create a list of words, sorted by their integer values
    sorted_list: List[str] = [word for word, _ in num_list_sorted]
    
    # Join the sorted list of words into a string, separated by spaces
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first creates a dictionary to map string representations of numbers to their integer values. It then splits the input string into a list of words, creates a list of tuples with each word and its corresponding integer value, sorts this list based on the integer values, and finally joins the sorted list of words back into a string. The result is the input string with numbers sorted from smallest to largest.