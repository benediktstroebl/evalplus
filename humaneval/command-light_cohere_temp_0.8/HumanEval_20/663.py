```python
from typing import List
def find_closest_elements(numbers: List[float]):
    closest1, closest2 = (min(numbers), max(numbers)) for i in range(len(numbers) - 1))
    return numbers[i], numbers[i+1] if numbers[i] < closest1 else numbers[i+1], numbers[i]
```
This code defines a function **find_closest_elements** that takes a list of numbers as input and returns a tuple containing the two closest numbers in the list. The function uses a min and max functions to find the two closest numbers and returns them in order. The function then uses the least number, larger number test to select the first and second closest numbers.