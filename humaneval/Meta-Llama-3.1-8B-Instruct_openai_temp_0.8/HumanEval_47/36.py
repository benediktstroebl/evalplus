```python
from typing import List

def median(numbers: List[float]) -> float:
    """
    Return the median of elements in the list numbers.
    
    If the list contains an even number of elements, the median is the average of the two middle numbers.
    
    :param numbers: A list of numbers.
    :return: The median of the numbers.
    """
    numbers.sort()  # Sort the list in ascending order
    n = len(numbers)  # Get the number of elements in the list
    
    if n % 2 == 1:  # If the list contains an odd number of elements
        return numbers[n // 2]  # Return the middle number
    else:  # If the list contains an even number of elements
        mid1 = numbers[n // 2 - 1]  # Get the first middle number
        mid2 = numbers[n // 2]  # Get the second middle number
        return (mid1 + mid2) / 2  # Return the average of the two middle numbers


def test_median():
    # Test cases
    assert median([3, 1, 2, 4, 5]) == 3
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0


if __name__ == "__main__":
    test_median()
    print("All test cases pass.")
```

This script defines a function `median` to calculate the median of a list of numbers. It uses the `sort` method to sort the list in ascending order, then checks whether the list contains an odd or even number of elements. If it's odd, it returns the middle number; if it's even, it returns the average of the two middle numbers. The script also includes test cases to verify the correctness of the `median` function.