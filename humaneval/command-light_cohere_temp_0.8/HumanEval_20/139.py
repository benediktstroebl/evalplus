```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # sort the list
    numbers.sort(key=lambda x: -x)
    # find the two closest numbers
    smallest = float('inf')
    second_smallest = float('-inf')
    for i in range(len(numbers) - 1):
        if numbers[i] < smallest and numbers[i] > second_smallest:
            smallest = numbers[i]
            second_smallest = numbers[i+1]
    return smallest, second_smallest

def test_find_closest_elements(numbers):
    # test the function
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 2]) == (1.0, 2.0)
assert find_closest_elements([1.0, 2.0, 3.0, 5.0, 2]) == (3.0, 2.0)
assert find_closest_elements([1.0, 1.0, 1.0, 2]) == (1.0, 1.0)
assert find_closest_elements([1.0, 2.0, 3.0, 4]) == (3.0, 4.0)
assert find_closest_elements([1.0, 1.0, 2, 3]) == (1.0, 2.0)
assert find_closest_elements([1.0, 2.0, 2, 3]) == (1.0, 2.0)
assert find_closest_elements([1.0, 3.0, 4]) == (1.0, 3.0)
assert find_closest_elements([1.0, 1.0, 2, 3]) == (1.0, 2.0)
assert find_closest_elements([1.0, 1.0, 1, 2]) == (1.0, 1.0)
assert find_closest_elements([1.0, 1.0, 1, 2]) == (1.0, 1.0)
assert find_closest_elements([1.0, 1.0, 1, 2]) == (1.0, 1.0)
assert find_closest_elements([1.0, 2.0, 3]) != (1.0, 3.0)
assert find_closest_elements([1.0, 2.0, 3]) != (1.0, 4.0)
assert find_closest_elements([1.0, 3.0, 4]) != (1.0, 4.0)```