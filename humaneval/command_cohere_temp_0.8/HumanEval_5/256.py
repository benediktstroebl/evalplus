```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimiter`, which is the number to be interspersed between elements of the list. 

It first creates an iterator `result` with a list comprehension, which conserves memory by filtering out the `delimiter` from the `numbers` list and converting the list to an iterator. Then, it determines the number of times the `delimiter` must be added to the `result` iterator using list comprehension and inserts that many delimiters into the `result` using the `extend` method. 

This approach ensures that the original list is not modified, and avoids the use of the `join` method, making the code more efficient and easier to understand.