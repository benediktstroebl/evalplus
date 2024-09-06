```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    # Determine the smallest and largest elements in the sorted list
    smallest = numbers[0]
    largest = numbers[-1]
    for num in numbers[1:-1]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest
```
This function takes a list of numbers and returns a tuple containing the two numbers that are closest to each other. The function sorts the list of numbers and then determines the smallest and largest elements in the sorted list. Finally, it returns the smallest and largest elements in that order.