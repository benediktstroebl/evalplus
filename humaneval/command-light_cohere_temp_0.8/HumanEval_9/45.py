Here's the self-contained Python function that generates a list of rolling max elements:
```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    max_rolling = [num for num in numbers if num >= max_num][-1:]
    rolling_max.append(max_num)
    return max_rolling
```
We've encapsulated the solution within a function, which provides self-containment and makes it easier to reuse and test the functionality.

Let me know if you'd like help with anything else!