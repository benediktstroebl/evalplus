```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   
    return result

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4,3,1]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]  # should be the unique elements

# run the function and run the test
numbers = [1, 2, 3, 2, 4,3,1]
print("Result:", remove_duplicates(numbers))
print("Expected:", [1, 3, 4])
```