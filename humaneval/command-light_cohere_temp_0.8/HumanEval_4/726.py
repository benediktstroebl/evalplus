```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Compute Mean Absolute Deviation 
    around the mean of this dataset. 
    MAD = average | x -x_mean | 
    """ 
    # your code here 
    return math.abs(sum((x -list(numbers) - numbers.mean())/len(numbers))
```
This script defines a function called `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation of the input list. It then passes all function with a sample list as an argument and prints out the result.