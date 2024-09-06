```python
from typing import List

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    smallest = float('inf') / 1
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
            smallest_index = index
        else:
            smallest = numbers[0]
            smallest_index = 0
    return smallest, smallest_index

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 2))

``` The function `find_closest_elements` takes a list of numbers and sorts them in ascending order. It then finds the smallest number and the index of the second number in the list. It then returns the smallest number and the index of the second number in the list.