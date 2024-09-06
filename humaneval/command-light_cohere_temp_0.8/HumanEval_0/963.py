Here's a Python script that solves the problem you described:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Initialize a dictionary to store elements' closeness results
    result = {}
    # Loop through the list of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                result[i] = result.append(numbers[j])
    return result
```
This function checks if any two numbers in the list are closer to each other than the given threshold. The function uses a Python dictionary to store the results, which is more efficient than iterating over the whole list.