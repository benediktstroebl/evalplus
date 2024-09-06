Here is a Python script that defines a self-contained function to calculate Mean Absolute Deviation (MAD):
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation 
    around the mean of this dataset
    """
    mean = sum(numbers)/len(numbers)
    MAD = sum(x - mean) / len(numbers)
    return MAD

def test_mean_absolute_deviation(test_list: List[float]) -> None:
    assert len(test_list) == 6
    assert mean_absolute_deviation(test_list) == 2.0
    assert abs(mean_absolute_deviation(test_list[:2]) - 1.0) < 0.1

def main() -> None:
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    test calculate MAD 
    assert mean_absolute_deviation(numbers) == 2.0
    assert abs(mean_absolute_deviation(numbers[:2]) - 1.0) < 0.1
    print("Test passed")
main()
```