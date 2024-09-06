Here is a self-contained Python script that solves the problem of checking if any two numbers in a list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list in ascending order
    numbers.sort(reverse=True, key=lambda x:x)
    # check if the two elements are closer than the threshold
    for i in range(1,len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i]-numbers[j]<threshold:
                return True
    return False
```
This script uses a list of floats and a given threshold to check if any two numbers in the list are closer than the threshold. It sorts the number and then loops over the list, checking if the difference between any two consecutive elements is less than the threshold. Then, it returns True.