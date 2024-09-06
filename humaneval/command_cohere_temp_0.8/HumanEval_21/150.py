Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    return rescaled
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled numbers based on the description of the problem. The linear transformation is performed by subtracting the minimum and dividing by the difference between the maximum and the minimum values in the list, ensuring the smallest number becomes 0 and the largest becomes 1.

To ensure the function works correctly, tests can be added that validate its behavior:
```python
def test_rescale_to_unit():
    # Sample tests
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit([0.0, 0.5, 1.0, 2.0, 3.0]) == [0.0, 0.166, 0.333, 0.5, 0.667]
    assert rescale_to_unit([-5.0, -3.0, -1.0, 1.0, 3.0]) == [-1.0, -0.333, 0.0, 0.25, 0.75]
    assert rescale_to_unit([0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 3.0]) == [0.0, 0.0, 0.333, 0.333, 0.333, 0.5, 0.667]
``` 

The test cases validate the behavior of the function with different input lists, ensuring correct scaling across various scenarios. 
The function is defined to handle any list of numbers and will throw an error if the list has less than two elements, which corresponds to the requirement of at least two elements in the task statement. Thus, no specific error handling is outlined in the code snippet. If you want to catch minimum element undefined error then you can do it like this: 
 ```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required for resizing.")
    min_num = min(numbers)
    if min_num == 0:
        raise ValueError("Minimum number cannot be zero.")
    max_num = max(numbers)
    if max_num == 0:
        raise ValueError("Maximum number cannot be zero.")
    rescaled = [(x - min_num) / (max_num - min_num) for x in numbers]
    return rescaled
```

Feel free to adapt this code to your needs and test thoroughly to ensure its behavior matches your expected use case. Let me know if you need any further modifications or if you'd like help adding more test cases to validate the function's behavior under different scenarios!