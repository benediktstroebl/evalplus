Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the solution:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

```python
# Test the function with a sample list of numbers
sample_numbers = [1.0, 2.0, 3.0, 4.0]
print(f"Mean Absolute Deviation for {sample_numbers}: {mean_absolute_deviation(sample_numbers)}")
```
This script uses the `numpy` library to provide a more efficient solution. It calculates the absolute deviations from the mean for each number in the input list, and then computes the mean of these absolute deviations to provide the Mean Absolute Deviation (MAD). The provided test case demonstrates how to use the function with a sample list of numbers.  Please note that this response assumes the presence of the `numpy` library, and you may need to install it if it's not already available in your environment (`pip install numpy`). 
If you don't have `numpy` available, let me know, and I can provide an alternative solution without external dependencies.