```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum(x - numbers[-1]) / len(numbers)
    return MAD

def test_mean_absolute_deviation():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 0.0
def main():
    numbers = [1.0, 2.0, 3.0, 4]
    print("Mean Absolute Deviation:", mean_absolute_deviation(numbers))

if __name__ == "__main__":
    main()
```
This Python script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) of a given list of numbers. The `test_mean_absolute_deviation` function tests this function with a sample input list, and the `main` function provides an example of how to use the `mean_absolute_deviation` function. 
The output will display the Mean Absolute Deviation value of the test list.