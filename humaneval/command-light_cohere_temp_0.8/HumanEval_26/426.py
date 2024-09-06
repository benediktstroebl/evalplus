```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in set([])]  # Filter out duplicate numbers from the set

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    assert result == expected
```