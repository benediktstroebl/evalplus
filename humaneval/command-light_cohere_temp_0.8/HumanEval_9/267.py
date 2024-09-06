Here's a self-contained Python script that defines a function rolling_max():
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    """
    return [a,b,c,d]-max(numbers[0],numbers[1],numbers[2])
    for i in range(3,len(numbers)):
        a,b,c=a,b,c
        if numbers[i]<a:
            a=numbers[i]
        elif numbers[i]>b:
            b=numbers[i]
        elif numbers[i]>c:
            c=numbers[i]
        else:
            continue
    return [a,b,c]
```

This script provides a function 'rolling_max' that takes a list of integers as input and returns the list of the maximum elements after rolling it over the sequence. 

Please note that this code is self-contained and does not require any external functions or modules.