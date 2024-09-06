Here's a solution:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # initialize a set to keep track of first occurrence of any element
    seen = set()
    for num in numbers:
        # check if num already seen
        if num in seen:
            return False
        seen.add(num)
    # check if any two elements are closer than the threshold
        if any( (num1, num2) in seen and (num1, num2) <= threshold):
            return True
    return False
```

This function takes two inputs: a List[float] called numbers, and a float threshold. It will then return True if it's the case that there are any two numbers in the list that are closer than the threshold. 

Also, this solution uses the set data structure to keep track of the elements and uses the <= operator to check if two elements are closer than the threshold.