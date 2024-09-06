```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [result])
    return result

# Test case 1
test_remove_duplicates = [1, 2, 3, 2, 4]
result = remove_duplicates(test_remove_duplicates)
assert result == [1, 3, 4]

# Test case 2
test_remove_duplicates = [4, 4, 4, 1]
result = remove_duplicates(test_remove_duplicates)
assert result == [4, 1]

# Test case 3
test_remove_duplicates = [10, 20, 30, 10]
result = remove_duplicates(test_remove_duplicates)
assert result == [10, 30, 10]
```
The script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function uses a set to keep track of seen elements and then adds elements to the result list that are not in the set. This script also includes several test cases to verify the correctness of the `remove_duplicates` function.