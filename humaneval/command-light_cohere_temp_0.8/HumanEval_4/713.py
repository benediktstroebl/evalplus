```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset
    """
    MAD = abs(x - numbers[int(len(numbers)/2.0)])
   
    sum([MAD for x in numbers[i+1:] for i in range(len(numbers))]))
    return MAD

# Test Case 1
numbers = [1.0,2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 1.0)

# Test Case 2
numbers = [0.5,0.0, 4,5]
print(mean_absolute_deviation(numbers) == 0.25)

# Test Case 3
numbers = [1,1,2]
print(mean_absolute_deviation(numbers) == 0.0)

```
This script defines a function **`mean_absolute_deviation(numbers: List[float])`** which takes a list of numbers and calculates the Mean Absolute Deviation (MAD) of the dataset. The MAD is calculated using the formula **`MAD = abs(x - numbers[int(len(numbers)/2.0)])`**. sum([MAD for x in numbers[i+1:] for i in range(len(numbers))]`). 

The script also has three test cases to check the correctness of the **`mean_absolute_deviation`** function.