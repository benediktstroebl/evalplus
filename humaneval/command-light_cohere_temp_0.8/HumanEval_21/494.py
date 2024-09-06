```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test: 
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0]) == [([0.0, 0.0, 0.0, 0])
   
    assert rescale_to_unit([1.0,2.0]) == [[[0.0, 0.0]])
   ``` 
This code defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list with the numbers in the range [0, 1].f]. The function uses the `typing` module to define a function that takes a list of numbers and returns a new list with the numbers in the range [0, 1.f]. 
To test the function, the code includes a series of `assert` statements that compare the output of the function with the expected output. 
The `assert` statements verify that the function is producing the correct output for the given input.