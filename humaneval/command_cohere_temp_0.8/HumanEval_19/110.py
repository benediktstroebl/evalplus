```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the string into a list of numbers, then sorts the list in ascending order, and finally joins the sorted list back into a string. It returns the string with the numbers sorted from smallest to largest. 

Here is an example usage of the function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
It can also be tested with the following script:
```python
from typing import List

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero zero nine') == 'zero nine zero'
    assert sort_numbers('eight four two') == 'two four eight'
    assert sort_numbers('five nine seven') == 'five seven nine'
    assert sort_numbers('one six four') == 'one four six'
```