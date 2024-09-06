```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until the given moment
    in the sequence.
    """
    list comprehension and rolling sum and max element technique for each number in the list.
    """
    list comprehension will rolling sum and max element technique for each number in the list
    numbers[:int(len(numbers)/2)] 
    = numbers[i::2] + numbers[(i+1):-1]
    return [max(numbers[i:int(len(numbers)/2)]) for i in range(len(numbers))]
    """
    return [max(numbers[i:int(len(numbers)/2)]) for i in range(len(numbers))]
```

The function rolling_max in the above code returns a list of integers that contains the maximum element in the list for each moment in the sequence. The max element is calculated using the max function, which takes an iterable and returns the maximum element in the iterable.