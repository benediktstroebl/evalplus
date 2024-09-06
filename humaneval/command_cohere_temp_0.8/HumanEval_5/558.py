```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result: List[int] = []
    for num in numbers:
        result.append(num)
        if len(result) < len(numbers):
            result.append(delimiter)
    return result
```

The `intersperse()` function takes in a list of integers, `numbers`, and an int `delimiter` as parameters. It uses a list comprehension to iterate through each number in `numbers`. For each number, it appends the number to the `result` list, which accumulates the interspersed output. After adding a number, it checks if the length of `result` is less than the length of `numbers`. If true, it adds the `delimiter` to the `result` list, ensuring that the `delimiter` is interspersed between consecutive elements of the input list. The function returns the `result` list once all numbers have been processed.  This approach ensures that `delimiter` is added at the appropriate intervals, creating the desired interspersed list.