```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation.
    MAD = average | x -x_mean|
    return MAD
    
    x = [1.0, 2.0, 3.0, 4.0]
    example is a = [1.1, 2.0, 3.0, 4.0]
   0 = 5.0
   5, 0.5.2, 6.0]
   0
    maximum possible1.0|
   0
   0) = 3.0
    sum(map(lambda x: abs(x-numbers['mean']) ))
    numbers['mean'] = sum(numbers)/len(numbers)
    return numbers['mean'] | numbers['x'] - numbers['mean'] |

test_cases = [ [ [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], [ [ [ [1.1, 0, 0], -1.0, -2.0, -3.0, -4.0] )
0)

print(mean_absolute_deviation(test_cases)))
```