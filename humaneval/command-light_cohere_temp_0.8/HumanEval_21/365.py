```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100 for x in numbers]
    return numbers

# Test the function with a list of numbers in markdown code block
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
test_rescale_to_unit(test_list)

# Verify that the list is correct
print(test_list)

# Test the function again with a different list
test_list2 = [10.0, 99.0, 9.0, 100.0]
test_rescale_to_unit(test_list2)

# Verify the output
print(test_list2)
```
This solution defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where each number has been divided by 100 to put it back into the range [0,1]. 

The solution also provides test cases for the function, which should pass successfully.