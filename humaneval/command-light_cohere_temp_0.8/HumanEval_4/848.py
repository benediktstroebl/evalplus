```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """
    Calculate Mean Absolute Deviation around the mean of this dataset
    MAD = average | x - x_mean |
    """
    mean = sum(numbers)/len(numbers)
    numbers.sort(x=num for num in numbers for x in [num-mean, num])
    return sum(abs(x)) / len(numbers)

def test_mean_absolute_deviation(numbers):
    return mean_absolute_deviation(numbers) == [1.0, 2.0, 3.0, 4.0])
```

numbers = [1.0, 2.0, 3.0, 4]
test_mean_absolute_deviation(numbers)

# True.