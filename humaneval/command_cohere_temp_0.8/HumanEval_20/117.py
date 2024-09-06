```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    return numbers[0], numbers[-1]
```

This function sorts the input list of numbers and returns the pair of the smallest and largest numbers in the list. It also validates the input list's minimum length of 2 to ensure the function's functionality. If the supplied list has less than 2 numbers, it raises a ValueError. 

Here is a simple test case:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
expected_result = (2.0, 2.2)

result = find_closest_elements(test_list)
assert result == expected_result
```

And here is another more elaborate test case:
```python
def test_find_closest_elements():
    # Single number case
    assert find_closest_elements([2.0]) == (2.0, 2.0)

    # Edge case: all numbers equal
    assert find_closest_elements([2.0, 2.0, 2.0]) == (2.0, 2.0)

    # Large list of numbers
    assert find_closest_elements([1.0, 2.0, 10.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Case with only two numbers
    assert find_closest_elements([10.0, 5.0]) == (5.0, 10.0)

    # Case with numbers closer to each other
    assert find_closest_elements([1.0, 2.0, 15.0, 16.0, 17.0]) == (2.0, 2.0)

    # Case with large range between smallest and largest
    assert find_closest_elements([0.1, 100.0]) == (0.1, 100.0)

    # Edge case: list with one element
    try:
        find_closest_elements([7.0])
    except ValueError as e:
        assert str(e) == "At least two numbers must be provided"

    # Null case
    assert find_closest_elements([]) == ()
```

This test case covers many scenarios and also includes a ValueError test for a list with only one element, which is less than the requisite minimum of two elements.