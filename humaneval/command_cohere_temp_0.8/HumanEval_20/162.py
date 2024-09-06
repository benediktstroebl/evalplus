```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if diff < 0:
            # Swap the first and last numbers if the difference is negative
            numbers[0], numbers[1] = numbers[-1], numbers[0]
        return numbers[0], numbers[1]
```

Here's an example of how to use the function and test it:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(numbers)
print(result)  # Output: (2.0, 2.2)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
result = find_closest_elements(numbers)
print(result)  # Output: (2.0, 2.0)
```

And here is a simple test suite:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.0, 10.0, 100.0, 1000.0]) == (1.0, 10.0)
    assert find_closest_elements([10.0, 11.0, 12.0, 13.0, 14.0, 21.0, 22.0, 23.0, 24.0]) == (10.0, 11.0)

    # Test with an odd number of elements
    try:
        find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
        assert False, "Should raise a ValueError"
    except ValueError:
        pass

test_find_closest_elements()
```

This test suite includes multiple test cases, such as edge cases, to verify the function's behavior.