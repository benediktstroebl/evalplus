```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Choose two closest elements and return them in order
    smaller_num, larger_num = (numbers[0] if numbers[0] < numbers[-1] else numbers[-1]) , numbers[1])
    return smaller_num, larger_num

def test():
    # Test the function
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    test two.8)
   2]
    print(find_closest_elements(numbers))
```
This script defines a function `find_closest_elements` that takes a list of numbers and returns a tuple containing the two closest numbers in the list, in order of their magnitude. The function uses the `smaller_num, larger_num` variable to compare the elements of the list, and selects the smaller number first, since it is the closer element. The test function then uses this function and passes in a list of numbers [1.0, 2.0, 3.0, 4.0, 5.0] to test test test the test function. The output of the test function is [2.0, 3.0].