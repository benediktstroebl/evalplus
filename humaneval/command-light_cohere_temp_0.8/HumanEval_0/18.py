Here's a solution to the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort(key=lambda x:math.abs(x - x))
    # Iterate through sorted list and check if two elements are closer than the threshold
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if math.sqrt(numbers[i]-numbers[j]) < threshold:
                return True
    return False
```

The above function sorts the given list of numbers and then iterates through the sorted list. Then, it checks if the elements of the current and next iteration are closer than the threshold or not. The function returns true if any two numbers in the list are closer to each other than the threshold, otherwise it returns false.