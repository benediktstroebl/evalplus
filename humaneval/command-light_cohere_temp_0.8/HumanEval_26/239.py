```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
# Tests:
>>> test_values = [1, 2, 3, 2, 4]
>>> remove_duplicates(test_values)
[1, 3, 4]
```

The function removes duplicate numbers from the input list and returns a new list with unique integers. It utilizes a set to keep track of numbers already encountered, ensuring that each number only appears once. The function also includes tests to validate its functionality.