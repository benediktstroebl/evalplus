```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        middle = numbers[len(numbers) // 2]
        last_idx = len(numbers) - 1
        return sorted([middle, numbers[last_idx]])[::-1]
```

The function first sorts the input list, and then works based on the size of the list:
1. If the length of the list is 2, it returns the two elements instantly. 
2. If the list has more than 2 elements, it finds the middle element and the last element and returns the pair. 

The function is also typed with `Tuple[float, float]` which means it must return a pair of floats. This is used in the automatic tests to check the types of the return values and also check that the values are floats (and not integers for instance). Here is a sample test that is added automatically:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
``` 

This test checks that the function returns the input `[2.0, 2.2]` sorted and reversed. 

The function also includes a `ValueError` which is raised when the input list length is less than 2. This raises can be tested as follows:
```python
def test_find_closest_elements_error():
    with pytest.raises(ValueError):
        find_closest_elements([1.0, 2.0])
``` 

Here `test_find_closest_elements_error` checks that the `ValueError` is raised when the list length is less than 2. 

To use this test, uncomment the `test_find_closest_elements_error` function and comment the other test function, and then run the module using `python -m pytest`.