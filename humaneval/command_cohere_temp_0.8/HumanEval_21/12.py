Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. This is achieved by calculating the linear factor as `((max-min)/(total_range))` and then applying this factor to each element in the list.

To test this function, one could write a test like the following:
```python
def test_rescale_to_unit():
    # Test list with more than 2 elements
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_rescale = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(numbers) == expected_rescale
```
In the test above, we provide a list where the expected rescaling corresponds to the manipulation of the factors as explained above. The `assert` statement will check if the `rescale_to_unit` function call results in the expected list. 
The code and test collectively illustrate the solution to the problem with a self-contained Markdown code block that can be exported to various formats. 
If there are other questions regarding the code, test, or problem solving strategies, feel free to ask!