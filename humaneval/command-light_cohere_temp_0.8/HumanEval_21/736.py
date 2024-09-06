```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n for n in numbers if n < 0]
    numbers.extend(0.0)
   0, (1.0, numbers[i] for i in numbers if i >= 0 and i != numbers[-1])
    return numbers

# Test cases 
# Test 1
input_nums = [0.5, 1.0, 0.0, -1]
print(rescale_to_unit(input_nums)) == [0.5, 1.0, 0.0, 1])

# Test 2
input_nums = [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
print(rescale_to_unit(input_nums)) == [0.1, 0.0, 0.0, 0.0, 0])

# Test 3
input_nums = [0.5, 0.5, 0.5, 1]
print(rescale_to_unit(input_nums)) == [0.5, 1.0, 0.0, 1])

# Test 4
input_nums = [0.5, 0.0, 0.5, 1]
print(rescale_to_unit(input_nums)) == [0.5, 0.5, 1.0, 0])

# Test 5
input_nums = [0.1, 0.0, 0.0, 0.0, 0]
print(rescale_to_unit(input_nums)) == [0.1, 0, 0, 0])
```

This function goes through each number in the list and adds 0.0 to any that is less than 0, and multiplies every other number by 1.0 to prevent negative scaling. The list is then rescaled by this linear transformation, such that it will return a list of numbers where 0 is the smallest and 1 is the largest.

To put it to the test, you can give it a list of numbers, and it will return the list with numbers that have been scaled according to this function.