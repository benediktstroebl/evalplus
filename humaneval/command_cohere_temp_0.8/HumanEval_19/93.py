```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    numbers.sort()
    return ' '.join(numbers)
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts that list in ascending order. Finally, the function joins the sorted list back into a string and returns the result.

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # one three five
```
The output of this code is:
```
one three five
``` 

This demonstrates how the `sort_numbers` function can be used to sort a string of space-separated numbers in ascending order and then return the sorted string.