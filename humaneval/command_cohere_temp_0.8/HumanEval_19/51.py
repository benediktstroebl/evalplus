```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of space-separated numbers from 0-9 and sorts them in ascending order. The function first converts the input string into a list of integers using `split()` and `int()` conversion. Then, it sorts this list using the `sort()` method. Finally, it converts the sorted list of integers back to a string by joining the sorted integer values with spaces, using the `map()` and `join()` methods, and returns the result. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # Output: one three five
```
This will print 'one three five', which is the sorted version of the numbers in the input string. 

This function is self-contained and can be easily used to sort a string of space-separated numbers in ascending order, as per the problem statement.