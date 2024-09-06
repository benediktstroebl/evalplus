```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the end of the sequence"""
    return [x for x,i in enumerate(numbers,1) if i.find(max(numbers[:i],numbers[(i+1)%len]))][::-1]
```
This function uses the `enumerize` function to enumerate over the list of integers, and uses the `find` method to determine if the maximum element in the current sublist, which starts at index `i`, matches the maximum element in the sublist starting at index `i+1`. If this is the case, the function returns the maximum element in reversed order.

Note that this solution uses the `typing` module to add type annotations to the function signature, which can help with better code readability and could potentially be used to generate more robust error messages in the function, if used in a IDE or other type checking environment.