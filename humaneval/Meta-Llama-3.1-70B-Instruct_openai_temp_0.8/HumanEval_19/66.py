```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Define a dictionary to map word numbers to their integer equivalents
    word_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of words
    word_numbers = numbers.split()

    # Convert the word numbers to integers and store them in a list of tuples
    # along with the original word numbers
    int_word_numbers = [(word_to_int[word], word) for word in word_numbers]

    # Sort the list of tuples based on the integer values
    sorted_int_word_numbers = sorted(int_word_numbers)

    # Extract the sorted word numbers from the list of tuples and join them into a string
    sorted_numbers =''.join([word for _, word in sorted_int_word_numbers])

    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of word numbers as input, converts them to integers, sorts them, and returns the sorted word numbers as a string. It uses a dictionary to map word numbers to their integer equivalents and sorts the word numbers based on these integer values. The test case at the end verifies that the function works as expected.