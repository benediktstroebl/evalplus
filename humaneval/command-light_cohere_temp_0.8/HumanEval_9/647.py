```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(numbers)  # Convert the input list to mutable object
    results = []
    
    for num in numbers:
        current_max = num
        for i in range(1, len(numbers)):
            if numbers[i] > current_max:
                current_max = numbers[i]
        results.append(current_max)
        
    return results
```
The function takes a list of integers as input and iterates through the list. Then, it maintains a running maximum element found in the sequence and appends the maximum element to the results list.

Note: This function is self-contained, meaning it can be used without relying on any other functions or modules. It is a way to solve the problem in a concise manner, using only the built-in functions of the Python language.