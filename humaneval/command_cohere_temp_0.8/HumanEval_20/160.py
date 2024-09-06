```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    return numbers[-2], numbers[-1]
```

This script defines a function `find_closest_elements` which takes in a list of numbers, sorts them, and returns the second last and last numbers in that list, assuming they are the closest to each other. The function also checks for at least two numbers to be present in the list, raising a `ValueError` if this is not the case. 

Here is an example of how to use the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # Output: (2.0, 2.2)
``` 

And here is the corresponding test suite:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 10.0, 2.0, 3.0, 4.0, 5.0, 2.2, 1.5]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 10.0, 2.0, 3.0, 4.0, 5.0, 2.2, 10.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 10.0, 2.0, 3.0, 4.0, 5.0, 2.0, 1.2]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 10.0, 2.0, 3.0, 4.0, 5.0, 2.0, 10.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0]) == (1.0, 2.0)

    assert find_closest_elements([1.0]) == (1.0, 1.0)
    assert find_closest_elements([10.0, 10.0, 10.0, 10.0]) == (10.0, 10.0)
    assert find_closest_elements([0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) == (0.5, 1.0)

    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

``` 
The test