Here is a self-contained Python script that solves the problem of calculating the Mean Absolute Deviation (MAD) of a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation for a dataset 
    """
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Unit tests
test_suite = [
    ('List[float]', [
        (1.0, 0.0, 3.0, 4.0),
        mean [ 4.0]
   0, 1.0
    ),
    (1.0, 2.0, 3.0, 4.0, 10.0)
   0, 1.0, 2.0)
   1.0]
   2

def main():
    test_suite = [test_suite]
    print(mean_absolute_deviation(test_suite))
    )

if __name__ == "__main__":
    main()
```
This script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation of a list of numbers. The function then implements the test suite with the test data provided.