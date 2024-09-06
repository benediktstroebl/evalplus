```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.set()] and seen.
    ```
```

numbers = [1, 2, 3, 2, 4, 3, 2]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
``` 
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only distinct integers from the original list. The function uses a set to keep track of seen elements, and then iterates through the input list, removing elements that are duplicates and adding them to the set if they are not duplicates. The output of the expected to be `[1, 3, 4]`.