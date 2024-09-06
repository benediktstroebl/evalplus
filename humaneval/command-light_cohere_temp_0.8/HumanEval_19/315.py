```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string is 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    Return the string with numbers sorted from smallest to largest
    """
    return sorted(numbers.split())
```
# Test the function with a few input strings 
 numbers = "three one five eight nine six".
expected = "one three five eight nine six"
actual = sort_numbers(numbers)
print(f"Expected: {expected}, Actual: {actual}")

# Test with input string containing invalid characters 
numbers = "2345 six seven eight nine";
expected = "six seven eight nine"
actual = sort_numbers(numbers)
print(f"Expected: {expected}, Actual: {actual}") 
```  This code contains a function called sort_numbers that takes a string of numbers and returns a sorted version of that string.  It then splits the use the string of numbers to be sorted.