```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter + n) for n in numbers
if __name__ == "__main__":
    numbers = [1, 2, 3]
    delimiters = [4, 4, 4]
    result = intersperse(numbers, delimiters)
    assert result == [1, 4, 2, 4, 3]
    assert len(result) == 7  # Ensure all numbers are present
    assert all(result[i] == i for i, c in enumerate(result, 1))  # Check consecutive elements
    assert all(result[i] == i for i in range(1, 5))  # Check non-consecutive elements
    assert result[-2:] len() == 2  # Ensure the last two elements aren't doubled
```