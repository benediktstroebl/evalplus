```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize closest and second closest to first element
    closest, second_closest = float('inf'), float('-inf')
    for i in range(1, len(numbers)):
        # Calculate the absolute difference between the current and the previous closest
        diff = abs(numbers[i] - numbers[i - 1])
        # If the difference is less than the current closest, update the closest
        if diff < closest:
            closest = numbers[i]
        # If the difference is less than the current second_closest, update the second_closest
        elif diff < second_closest:
            second_closest = numbers[i]
    # Return the closest and second_closest in that order
    return closest, second_closest
```
The code takes a list of floating-point numbers as input and uses two variables, `closest` and `second_closest`, to store the two closest numbers. The `closest` variable is updated based on the current number in the list and the `second_closest` variable is updated based on the current number if the absolute difference between the current number and the previous number is less than the `closest`. The `second_closest` variable is then returned, and the function returns the `closest` and `second_closest` variables in that order.