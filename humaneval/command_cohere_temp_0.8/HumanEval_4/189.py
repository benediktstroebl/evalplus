Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script utilizes the `numpy` library, ensuring efficiency in handling numerical operations, especially for large datasets.

Here's an example of using the `mean_absolute_deviation` function:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
The output will be:
```
1.0
```
This value corresponds to the Mean Absolute Deviation of the provided example list.