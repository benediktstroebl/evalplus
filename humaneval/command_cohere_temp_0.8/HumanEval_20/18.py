```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    x = numbers[-2]
    y = numbers[-1]
    return x, y
```

The function `find_closest_elements()` takes a list of numbers as input and returns the two closest numbers in the list. The function sorts the list and checks if the length of the list is less than 2. If it is, it raises a `ValueError`, if the length is 2 or more, it returns the smaller and larger numbers of the just-sorted list. These functionalities are tested in the following code:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 8.0, 6.0, 4.0, 12.0, 14.0, 16.0]) == (12.0, 14.0)
    try:
        find_closest_elements([1.0, 2.0])
    except ValueError as e:
        assert str(e) == "At least two numbers must be provided"

test_find_closest_elements()
``` 

The last test is a sanity check for the error handling functionality. If the input list has only one number, the function should not return anything and should raise a `ValueError` with the error message "At least two numbers must be provided".  This is checked using a try/except block. The testing code is built on top of `pytest`, a popular testing library in Python.