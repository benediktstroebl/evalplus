```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string containing the same numbers sorted in ascending order. 

Here is an explanation of the code:
- The function `sort_numbers` takes a string value `numbers` as input. 
- The line `numbers = [int(char) for char in numbers.split()]` transforms the string into a list of integers. The `.split()` method separates the string into a list of words, and the `int()` function converts each word into an integer.
- The `sort()` method sorts the integers in ascending order.
- The `return ' '.join(map(str, numbers))` line joins the sorted integers back into a string and returns the result.

This algorithm will work correctly for any input string containing numbers from 0 to 9, including both positive and negative integers.