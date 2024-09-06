```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The function `remove_duplicates` takes a list of integers as input and returns a list of unique integers from the input list. It maintains order in the output list. This function uses a set, `seen`, to efficiently track encountered integers and avoid duplicates. It moves through the input list, adding each integer to the result list and the `seen` set only if it hasn't been seen before or if keeping it wouldn't result in a duplicate.

Here's a simple test case to verify the function:
```python
test_list = [1, 2, 3, 2, 4]
expected_result = [1, 3, 4]
result = remove_duplicates(test_list)
print(result)  # Expected output: [1, 3, 4]
assert result == expected_result
```