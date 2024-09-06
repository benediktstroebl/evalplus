```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(key=lambda x: x, -x)
    # Find the two closest elements
    i = 0
    j = len(numbers) - 1
    while i < j:
        while numbers[i] < numbers[j] and i < j - 1:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
        i += 1
        j -= 1
    # Return the two closest elements
    return numbers[i], numbers[j]
```
This function takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other. The function first sorts the array in ascending order and then uses a while loop to find the two closest elements. The loop stops when the minimum number is found and the maximum number is outside the range. The function then returns the numbers[i] and numbers[j] as the two closest elements.