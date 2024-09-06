Here is a Python script that contains a self-contained function that solves the problem of finding the closest elements from a list of numbers in markdown code:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Find the two closest elements in the list and return them in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    
    comparison_scores = []
    for i in range(1, len(numbers)):
        current_distance = numbers[i] - numbers[i - 1]
        comparison_scores.append(current_distance)

    min_distance, max_distance = float('inf'), float('-inf')
    for i in range(len(comparison_scores)):
        if comparison_scores[i] < min_distance:
            min_distance = comparison_scores[i]
        if comparison_scores[i] > max_distance:
            max_distance = comparison_scores[i]

    return numbers[min_distance], numbers[max_distance]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = find_closest_elements(numbers)

print(result)
```

This script provides a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function first checks if the list has less than two elements, and if so, it returns the first and second element in the list. Then, it calculates the distance between the elements and compares it with the maximum and minimum distance from the previous iteration. The function iterates through the elements, calculating the distance and updating the minimum and maximum distances. Finally, it returns the two elements that are the closest to each other.