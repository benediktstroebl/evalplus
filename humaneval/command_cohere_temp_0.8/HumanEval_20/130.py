```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return _get_closest_pair(left, right)


def _get_closest_pair(a, b):
    if abs(a - b) < min(abs(a - _min(a, b)), abs(b - _min(a, b))):
        return (_min(a, b), _max(a, b))
    else:
        return (_min(_min(a, b), _min(b, a)), _max(_max(a, b), _max(b, a)))


def _min(a, b):
    if a < b:
        return a
    else:
        return b

def _max(a, b):
    if a > b:
        return a
    else:
        return b

```

The test cases assume the usage of the `find_closest_elements` function and check if the result is expected:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 12.0]) == (20.0, 22.0)
    assert find_closest_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5]) == (1.1, 1.5)
    assert find_closest_elements([0.0, 0.1, 0.2, 0.3, 0.4, 0.5]) == (0.1, 0.5)
    assert find_closest_elements([-10.0, -9.0, -8.0, -7.0, -6.0, -5.0]) == (-10.0, -5.0)
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 52.0]) == (10.0, 52.0)
``` 

The code assumes that every element in `numbers` is unique and doesn't repeat, if those conditions are not fulfilled, it might impact the correctness of the code. 
The `find_closest_elements` function first sorts the input list, then finds the middle number of the list using integer division (`len(numbers) // 2`), and then uses these middle numbers and their neighbors to the left and right as candidates for the closest pair.  The `_<>_<>` helper function compares two numbers and returns the smaller and the larger of the two if they are equal, and `_min` and `_max` also handle the comparison of two numbers.  Lastly, the `_get_closest_pair function uses the logic to determine if the difference between the candidates is smaller than the smaller of the two or larger of the two absolute differences, and decides