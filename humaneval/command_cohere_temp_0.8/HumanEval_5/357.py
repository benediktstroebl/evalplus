```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter`. It first filters out the `delimiter` from the list using a list comprehension, then extends the list to its original length by inserting `delimiter` units to ensure the appropriate spacing. This approach ensures that the resulting list has the desired delimiters without iterating through the list multiple times.