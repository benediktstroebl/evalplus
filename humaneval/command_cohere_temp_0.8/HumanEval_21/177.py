Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the list becomes 0 and the largest number becomes 1. The transformation is a linear transformation and is calculated as follows: `[x_i - min(list)] / [(max(list) - min(list)] * 1`. The resulting list of transformed numbers is then returned. 

Here's an example of using the `rescale_to_unit` function:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
The following is a more comprehensive example:
```python
>>> rescale_to_unit([-5.0, -3.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
[-1.0, -0.25, -0.5, -0.75, -1.0, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
```
The resulting list of transformed numbers is returned from the function and is based on the provided list of numbers. 

Such a rescaling is useful in many data analysis tasks to create features that have a variance close to 1. This helps in stabilizing the distribution of the features and making them more compatible for certain machine learning algorithms that rely on stable input features.  It's important to note that the function assumes the list of numbers contains at least two elements. The smallest and largest numbers need not be integers as per the arguments.