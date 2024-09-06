```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if diff > 0:
            return numbers[0], numbers[-1]
        else:
            middle = (len(numbers) - 1) // 2
            left, right = numbers[middle], numbers[0]
            return _find_closest(left, right, numbers[1: middle + 1]) or \
                  _find_closest(left, right, numbers[middle + 1:])

def _find_closest(a, b, numbers):
    for n in numbers:
        if abs(a - n) < abs(b - n):
            b = n
        elif abs(a - n) > abs(b - n):
            a = n
    return a, b
```

The test cases are not included but can be added to see if the function behaves as expected. The tests could be something like this:
```python
def test_find_closest_elements():
    # Test case 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
    expected = (2.0, 2.2)
    assert find_closest_elements(numbers) == expected

    # Test case 2
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
    expected = (2.0, 2.0)
    assert find_closest_elements(numbers) == expected

    # Test case 3
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 5.0, 2.2]
    expected = (5.0, 2.2)
    assert find_closest_elements(numbers) == expected

    # Test case 4
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 2.2]
    expected = (4.0, 2.2)
    assert find_closest_elements(numbers) == expected

    # Test case 5
    numbers = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    expected = (1.0, 1.0)
    assert find_closest_elements(numbers) == expected

    # Test case 6
    numbers = [0.1, 1.0, 2.0, 3.0, 4.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.1]
    expected = (0.1, 5.0)
    assert find_closest_elements(numbers) == expected

test_find_closest_elements()
```
The function will return the closest elements while also preserving the order of being the smaller or larger number. So in case one of them is the same, it will still return these two numbers.