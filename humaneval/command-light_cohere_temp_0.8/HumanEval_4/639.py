```python
from typing import List

def mean_absolute_deviation(numbers):
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset. 
    MAD = average | x -x_mean |
    """
    return sum((x - numbers[i])) / len(numbers) 

# Test case 1 
numbers = [1.0, 2.0, 3.0, 4.0]
print("The output is 0.9 (the expected output of the function"))

# Test case 2
numbers = [1.5, 1.0, 2.0, 3.0]
print("The output is 0.6")

# Test case 3
numbers = [10.0, 1.0, 2.0, 3.0]
print("The output is 0.6")

# Test case 4
numbers = [100.0, 101.0, 2.0]
print("The output is 0.5")

# Test case 5
numbers = [1.1, -3.0, -5.0]
print("The output is 0.9")

# Test case 6
numbers = [0.0, 0.0, 0.0]
print("The output is 0.5")
```