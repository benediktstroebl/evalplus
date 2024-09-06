Here is a Python script that checks for elements in a given list of numbers that are closer to each other than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Initialize two lists to store the distance between each pair of numbers.
    distances = [[0] * (len(numbers) - 1)]
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            distances[i][j] = (numbers[j] - numbers[i])**2
    distances[i][j] += distances[i][j-1]  # accumulation
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if distances[i][j] < threshold:
                return True
    return False
```
The function checks if in a list of numbers, any two numbers are closer to each other than a given threshold. The script uses the for this complexity and will return true if there are any two numbers in the list that are closer than the given threshold, and false otherwise.