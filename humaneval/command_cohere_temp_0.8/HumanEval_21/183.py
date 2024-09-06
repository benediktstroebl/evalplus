Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [x / max(numbers) for x in numbers]
```
The function `rescale_to_unit` divides each number in the list by the maximum number in the list, thereby ensuring that the largest number becomes 1, and the smallest number becomes 0. 

This approach takes advantage of the List Comprehension, a concise way to create a new list based on the values of an existing list. Here, it transforms each element of the original list `numbers` by dividing it by the maximum value, achieving the desired linear transformation. 

To test this function, you can run the following code: 
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
assert rescale_to_unit(test_list) == expected_result
```
The function is validated successfully if the assertion passes without any errors.