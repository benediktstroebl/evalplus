```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if abs(diff) < 1e-6:
            return (numbers[0], numbers[0])
        else:
            return (numbers[0], numbers[-1])
```
The function first sorts the input list of numbers and checks if the list has at least two elements. If the length of the list is less than 2, it raises a ValueError, indicating that at least two numbers must be provided. Otherwise, it checks if the difference between the first (smallest) and last (largest) elements is less than 1e-6. If they are almost equal, it returns either number twice (smallest first). If they are not equal, it returns the smallest and largest numbers as requested in the challenge. 

Here is a simple test suite to confirm it behaves as expected:
```python
def test_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 20.0, 21.0, 22.0, 23.0, 24.0]) == (10.0, 20.0)
    assert find_closest_elements([1.0, 1.1, 1.2, 1.3, 1.4, 1.5]) == (1.1, 1.5)
```