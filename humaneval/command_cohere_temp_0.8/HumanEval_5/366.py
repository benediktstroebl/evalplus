```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an int `delimiter` as inputs. It constructs a new list `result` where it iterates through the elements in `numbers`, excluding the `delimiter` from the final list. It then extends the `result` list with duplicates of `delimiter` based on the calculation `len(numbers) - len(result)` to ensure that all empty spaces between numbers are filled with the `delimiter`. The function returns the `result` list. 

This function solves the problem of inserting a delimiter between every two consecutive elements of a list and is encapsulated within a self-contained Python script.