```python
from typing import List

def mean_absolute_deviation(numbers):
    """ 
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset. 
    MAD = average | x -x_mean |

    Test: 
    Given a list [1.0, 2.0, 3.0, 4.1] 
    Return print(fails to pass this test: [1.0, 3.0, 4.0])

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0) 
    """ expected output: True
    Test: 
    Given a list [0.0, 0.0, 0.0]
   0.0,
   0.0] 
    print(fails to pass this test: [0.0, 0.0, 0.0])
    print(mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0)
   Also, we can print(mean_absolute_deviation([0.0, 0.0, 0.0]) == 0.0) 
    Test: 
    Given a list [1.0, 2.0, 3.0, 4], 
    print(fails to pass this test: [1.0, 3.0, 4]) 
    print(mean_absolute_deviation([1.0, 2.0, 3]) == 2.0) 
print(mean_absolute_deviation([1.0, 3.0, 4]) == 3.0) 
```