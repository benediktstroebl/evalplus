```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the two closest numbers and the distance
    closest_num, closest_distance = (numbers[0] if numbers[0] < numbers[1] else numbers[1]) , (numbers[1] if numbers[0] < numbers[1] else numbers[0])
    closest_distance = abs(numbers[0] - numbers[1])
    # Return the two closest numbers in the list
    return (numbers[0], closest_distance) if (numbers[0] if numbers[0] < numbers[1] else numbers[1]) == closest_distance else (numbers[1], closest_distance)
    ```