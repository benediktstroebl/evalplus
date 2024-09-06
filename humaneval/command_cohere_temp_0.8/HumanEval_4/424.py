Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` calculates the absolute deviation of each number in the input list from the mean of the list, and then returns the average of these deviations. This is done using NumPy's efficient array operations and built-in `mean` function.

To test this function, you can create a test list of numbers and assert that the result is close to the expected mean absolute deviation:
```python
numbers = [1., 2., 3., 4.]
expected = np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
assert np.isclose(mean_absolute_deviation(numbers), expected)
```

To run this code, you'll need to install NumPy:
```bash
pip install numpy
```

You can then run the test script. This approach utilizes NumPy's functionalities to efficiently handle the computations, making the function more scalable and faster when dealing with large datasets.