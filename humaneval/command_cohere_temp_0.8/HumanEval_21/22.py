Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [x / min(numbers) for x in numbers]
    return [val * len(numbers) for val in rescaled]
```
This rescales the list to have the smallest number mapped to 0 and the largest number mapped to len(numbers) with a linearly scaled progression in between.

To test this function, you can use the following code:
```python
from deepdiff import DeepDiff 

test_lists = [
    [1.0, 2.0, 3.0, 4.0, 5.0], 
    [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 
    [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
] 

expected_rescaled = [
    [0.0, 0.25, 0.5, 0.75, 1.0], 
    [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0], 
    [0.0, 0.05555, 0.13889, 0.22222, 0.30303, 0.384615, 0.461538, 0.537692, 0.615385, 0.698412, 0.783241, 0.862074, 0.922137, 1.0]
] 

for idx, test_list in enumerate(test_lists):
    assert DeepDiff(rescale_to_unit(test_list), expected_rescaled[idx]) == {}
```
This code uses the DeepDiff function to assert that the output from the function `rescale_to_unit` matches the expected output for a variety of input lists.