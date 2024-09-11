```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Define a dictionary to map word numbers to their integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    words = numbers.split()
    
    # Use a lambda function to sort the list based on the integer value of each word
    sorted_words = sorted(words, key=lambda word: number_map[word])
    
    # Join the sorted list back into a string
    sorted_numbers =''.join(sorted_words)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one'))  
# Output: 'one two three four five six seven eight nine'
print(sort_numbers('zero five two three eight six nine'))  
# Output: 'zero two three five six eight nine'
```

This script solves the problem by first splitting the input string into a list of words, then sorting that list based on a dictionary that maps word numbers to their integer values, and finally joining the sorted list back into a string. The result is a string with the numbers in the correct order from smallest to largest.