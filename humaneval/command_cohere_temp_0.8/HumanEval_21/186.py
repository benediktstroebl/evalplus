Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This function can be used to normalize data for analysis or visualization. The unit tests for this function would typically assert that the output list is correct for a given input list. 
For example, let's say that we have the following input list: `[1.0, 2.0, 3.0, 4.0, 5.0]`
Then this is how it would work:
```python
input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_list = rescale_to_unit(input_list)
print(rescaled_list)
```
The output would be:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
``` 

This is the expected output based on the problem statement. The function correctly calculates the rescaling factor as the ratio of the largest to the smallest element, then applies this factor to every element in the list, resulting in the desired normalized list. 

This approach has a time complexity of `O(n)` since it requires iterating over the input list once to compute the minimum and maximum values, and then iterating over the input list again to perform the normalization. This is a simple and efficient approach for small to medium-sized lists.