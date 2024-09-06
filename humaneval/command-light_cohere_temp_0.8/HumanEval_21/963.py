```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0
    return the numbers, but the smallest number is 0 and the largest is 1.
    }

# Test cases:
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = [1.0, 2.0, 3.0, 4]
numbers = [1.0, 2.0, 3.0, 4]
numbers = [1.0, 0.0, 0]
numbers = [1.0, 0, 0]
numbers = [1.0, 2.0, 3.0, 4]
numbers = [1.0, 0, 0]
numbers = [1.0, 0, 0]
numbers = [0, 0, 1.0]
print(rescale_to_unit(numbers))  # Output: [0, 0.0, 1.0]

print(rescale_to_unit([1.0, 2.0, 3.0, 4]))  # Output: [0.0, 0.0, 0.0]
print(rescale_to_unit([1.0, 2.0, 3]))  # Output: [0.6, 0.0, 0.0]
print(rescale_to_unit([1.0, 0]))  # Output: [1.0, 0, 0]
print(rescale_to_unit([1.0]))  # Output: [0.0, 1.0, 0])
print(rescale_to_unit([1.0, 1.0]))  # Output: [0.0, 1.0, 0]
print(rescale_to_unit([1.0]))  # Output: [1.0, 0, 0])
print(rescale_to_unit([1.0, 2.0]))  # Output: [0.0, 1.0, 0]
print(rescale_to_unit([1.0, 2.0]))  # Output: [0.0, 1.0, 0]
print(rescale_to_unit([1.0, 3]))  # Output: [0.0, 0, 1.0]
print(rescale_to_unit([2.0, 3]))  # Output: [1.0, 0, 1.0]
print(rescale_to_unit([2.0, 0]))  # Output: [1.0, 0]
print(rescale_to_unit([0.0, 3]))  # Output: [0.0, 1.0, 0]
print(rescale_to_unit([0.0]))  # Output: [0.0, 1.0, 0])
print(rescale_to_unit([0.0]))  # Output: [0.0, 1.0, 0])
print(rescale_to_unit([0.0]))  # Output: [0.0, 0.0, 1.0])  #