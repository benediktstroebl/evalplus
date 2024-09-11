```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numbers from 'zero' to 'nine' 
    as input, and returns the string with numbers sorted from smallest to largest.
    
    Parameters:
    numbers (str): A space-delimited string of numbers.
    
    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their numerical values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    word_list = numbers.split()
    
    # Replace each word with its corresponding numerical value
    num_list = [num_dict[word] for word in word_list]
    
    # Sort the list of numbers
    sorted_num_list = sorted(num_list)
    
    # Replace each number with its corresponding word
    sorted_word_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted_num_list]
    
    # Join the sorted list of words into a string separated by spaces
    sorted_string =''.join(sorted_word_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('nine four two'))
print(sort_numbers('zero eight seven'))
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine' as input, and returns the string with numbers sorted from smallest to largest. It uses a dictionary to map number words to their numerical values, splits the input string into a list of words, replaces each word with its corresponding numerical value, sorts the list of numbers, replaces each number with its corresponding word, and joins the sorted list of words into a string separated by spaces. The function is then tested with several examples.