Here's a self-contained Python script that solves the problem:
```python
from typing import Dict

# Dictionary to map words to numbers for easy comparison
NUMBERTOWORD: Dict[str, str] = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of words
    num_list = numbers.split()

    # Use the dictionary to map words to numbers and sort the list
    sorted_num_list = sorted([(NUMBERTOWORD[word], word) for word in num_list])

    # Sort the list by the numbers (first element of each tuple)
    sorted_num_list.sort(key=lambda x: int(x[0]))

    # Return the sorted list as a space-delimited string of words
    return''.join([word for _, word in sorted_num_list])

# Test the function
if __name__ == "__main__":
    print(sort_numbers('three one five'))  # Output: 'one three five'
    print(sort_numbers('nine five one'))   # Output: 'one five nine'
```
This script defines a dictionary `NUMBERTOWORD` to map words to numbers for easy comparison. It then splits the input string into a list of words, maps each word to its corresponding number, sorts the list, and returns the sorted list as a space-delimited string of words.