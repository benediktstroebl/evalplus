```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(dict.fromkeys(numbers))
```

This Python script provides a function called `remove_duplicates`, which takes a list of integers as input and returns a new list that excludes any duplicate integers. To achieve this, it uses a dictionary where the keys are the unique elements, and the values are not relevant in this case. The `dict.fromkeys()` method is employed to create this dictionary from the input list of integers, effectively eliminating any duplicate elements whilst preserving the original order. The function outputs the resulting unique integer list.

Here is an example usage of the function:
```python
print(remove_duplicates([1, 2, 3, 2, 4])) 
```

And its test case could be:
```python
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == [0, 1, 2, 3, 4]
```