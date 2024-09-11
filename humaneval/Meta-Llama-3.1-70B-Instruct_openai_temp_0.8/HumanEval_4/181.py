```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a given dataset.

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The Mean Absolute Deviation of the input dataset.
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation of {numbers} is {mad:.2f}")

# Self-contained script to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([10.0, 20.0, 30.0, 40.0], 10.0),
        ([5.0, 5.0, 5.0, 5.0], 0.0),
    ]

    for test_case in test_cases:
        numbers, expected_mad = test_case
        mad = mean_absolute_deviation(numbers)
        assert round(mad, 2) == expected_mad, f"Expected MAD of {numbers} to be {expected_mad}, but got {mad}"
        print(f"MAD test for {numbers} passed.")
```