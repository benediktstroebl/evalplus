```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes a list of numbers `numbers` and an int `delimiter` as input and returns a list where each number is either interspersed with the `delimiter` or returned as it is if the delimiter is not present in the number. The algorithm achieves this in a Pythonic style by:
1. Creating a list `result` to house the return values bypassing all elements of `numbers` if they are not equal to the `delimiter`.
2. `result.extend` is used to insert `delimiter` multiples times to the list `result`, the number of times is calculated as `len(numbers) - len(result)` so as to intersperse the `delimiter` between each element of `numbers`.

This function returns the interspersed list if both `numbers` and `delimiter` are of type `int`.