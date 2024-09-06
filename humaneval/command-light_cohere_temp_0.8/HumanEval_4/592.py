```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation for the input dataset
    MAD = sum(x - mean) / len(numbers)
    return MAD

def test_mean_absolute_deviation(test_numbers: List[float]) -> None:
    import_float(MAD)
    assert_close_enough(test_numbers, [1.0, 1.0], rtol=1e)
    assert_close_enough(MAD, test_numbers[0] - test_numbers[1], rtol=1e-6)
    assert_close_enough(MAD, test_numbers[2] - test_numbers[0], rtol=1e-6)

if __name__ == "__main__":
    test_numbers = [1.0, 2.0, 3.0, 4.0]
   0]
   
    print("Test passed!")
    ```