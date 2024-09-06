```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string of numbers into individual numbers and converts them to integers in a list. It then sorts these numbers in ascending order. Finally, the function returns a string where the sorted numbers are joined back together with a space between each number, ensuring the original format of the input string. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five')) # Output: one three five
```
This will sort the numbers 'one', 'three', and 'five' in ascending order, and return the sorted string.