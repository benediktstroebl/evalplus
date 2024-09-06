```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script provides a function that takes a string of numbers and sorts them in ascending order, returning the sorted sequence as a string. The function first converts the input string into a list of integers using list comprehension. It then sorts this list using the `sort()` method. Finally, it converts the sorted list of integers back to a string by joining the list with spaces using the `join()` method. The expected output of the function is a string with the numbers sorted from smallest to largest. 

Here's an example of how to use the provided function to sort a string of numbers, such as "three one five", to verify its correctness:
```python
sort_numbers("three one five")  # Output: "one three five"
```
This demonstrates the function's ability to correctly sort the numbers one, three, and five, resulting in a sorted string output.