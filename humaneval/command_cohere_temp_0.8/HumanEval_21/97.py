Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0 and the largest number becomes 1. This is achieved by calculating the minimum and maximum values in the input list, and applying a linear transformation to the numbers based on these min and max values. The test cases verify that the function behaves as expected, and the `>>>` notation is used as an example of how the function can be invoked and test the resulting values.  This approach ensures the list of numbers is normalized with values ranging between 0 and 1.  The implementation is concise and accomplishes the task efficiently.  It can be used in various applications like data preprocessing for machine learning or visualization to adapt data ranges.  It can also be easily extended to handle other data types or additional logic, like scaling by a different factor or applying a nonlinear transformation, by modifying the transformation logic.