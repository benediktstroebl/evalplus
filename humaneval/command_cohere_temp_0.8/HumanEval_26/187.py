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

The function `remove_duplicates` takes a list of integers as input and returns a list of unique integers from the input list. It uses a set called `seen` to keep track of the unique integers it has encountered so far. It iterates over the input list, and for each integer `num`, it checks if the integer is already in the `seen` set. If the integer is not in the set, or if the set contains only one element at this point, it adds the integer to the `result` list and adds it to the `seen` set. This way, the function constructs a list containing only the unique integers from the input list, with elements arranged in the same order as in the input. 

Here is a simple test to check the functionality of the function:
```python
test_remove_duplicates = {
    "test_simple": {
        "description": "Test removing duplicates from a list",
        "input": [1, 2, 3, 2, 4],
        "expected_output": [1, 3, 4]
    }
}
``` 

This test verifies that the output of the function matches the expected output for a specific input list.