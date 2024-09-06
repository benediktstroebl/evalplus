```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    ``` 
The function takes a string of numbers separated by spaces as input and returns a sorted version of that string. The function then loops through each character in the string, converts it to an integer using int(), and adds it to the list of numbers. Then, the function sorts the list of numbers using the sorted() function and returns the sorted string.