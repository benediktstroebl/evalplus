```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in a list of numbers `numbers` and an int `delimiter` and returns a new list where each element of `numbers` is separated by `delimiter`. If `delimiter` appears in the list, it is skipped. The markdown code block at the top describes the problem and can be copied and pasted into a Jupyter Notebook or a .py file to test the function.  This solution has a time complexity of O(n) where n is the length of the input list `numbers`. It achieves this by only filtering out the delimiter from the list which has a complexity of O(n) and then performing an equal number of appends which also has a complexity of O(n).