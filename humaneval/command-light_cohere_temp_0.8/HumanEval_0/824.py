```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers in ascending order
    numbers.sort(key=lambda x: x, reverse=(threshold>x))
    # Check for two adjacent numbers that are less than the threshold
    for i in range(1,len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[j] - numbers[i] < threshold:
                return True
    return False
```
This function uses two nested loops to iterate over the list of numbers and compare each number to the previous one, if any two numbers are closer to each other than the threshold, the function returns True, otherwise it returns False. 

You can test this function with different lists of numbers and thresholds to verify its correctness.