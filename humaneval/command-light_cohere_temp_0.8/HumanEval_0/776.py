```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Loop through list of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # If the difference between two numbers is less than or equal to the threshold
            if math.abs(numbers[i]-numbers[j]) <= threshold:
                return True
    return False
```
This function takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than each other than the threshold. It uses a loop to compare each pair of numbers in the list and checks if the absolute difference between them is less than or equal to the threshold. 

You can use this function to check for elements that are closer than a certain threshold in a given list.