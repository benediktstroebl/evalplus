```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
   
         [ convert_the_numbers -> a list
        of numbers, then sort the list
        (using the sort() builtin method), then join the list back into a string."""
    return " ".join(sorted(numbers.split()))

# Test
numbers = "three onefive"
print(sort_numbers(numbers))  # Output: one threefive 

``` 
This script defines a function called sort_numbers that takes a space-delimited string of numbers from zero to nine as input and returns the string with the numbers sorted from smallest to largest. The function uses the split() to convert the input string into a list of numbers, sorts the list, and then joins the sorted list back into a string.