```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.set()] and seen.
    ```
```

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # expected output: [1, 3, 4]
``` 
This function uses a set to keep track of duplicate numbers, then loops through the input list and adds any elements not already in the set to the result list.