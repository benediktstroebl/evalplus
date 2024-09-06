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
    if (a == b) or ((a + b) / 2.0 in [x for x in sorted(set(numbers)) if x != a and x != b]):
        return a, b
    else:
        return _get_closest_pair(a, b - (b - a)) if a != b else a, a
```

The tests would look like this:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 8.0, 6.0, 4.0, 12.0, 14.0, 16.0]) == (12.0, 12.0)
    assert find_closest_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) == (1.9, 2.0)
    assert find_closest_elements([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]) == (15.0, 15.0)
```

The rationale behind the approach is to first sort the input list and then identify the middle two elements. If these are equal or one is an exact average of the two, then we have found our closest pair. If not, we recursively search for the closest pair between the left and right element, but this time we offset the right value by the difference between the two, to ensure we are always looking at the closest points. This algorithm optimally finds the closest pair with a time complexity of O(n log n) where n is the length of the input list, as we are always working with a sorted list and regularly cutting the list in half.  If the recursion is optimized, the maximum depth will be log(n) and at each level we process a list of size n/2, so overall the complexity is O(n log n).  If we only cared about the result being correct, we could optimize the recursion using memoization to avoid some recursive calls and make the maximum depth more linear in terms of the input size.  This would be less efficient in terms of memory usage, but the time complexity would be O(n).  Please let me know if you would like this additional explanation or any more examples of how to extend or improve the tests.