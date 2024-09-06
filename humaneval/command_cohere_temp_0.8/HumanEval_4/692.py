Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

And here is a bash script that applies this function to a usage example, and verifies correctness against expected output with pytest:
```bash
#!/bin/bash

python -c "import numpy as np; import pandas as pd; from typing import List; def mean_absolute_deviation(numbers: List[float]) -> float: return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers)))); numbers=[1.0, 2.0, 3.0, 4.0] mean_absolute_deviation(numbers)"
 pytest -vs tests/test_mean_absolute_deviation.py
```

The Python script defines a function that calculates the mean absolute deviation of a list of numbers. The bash script applies this function to an example and verifies its correctness against the expected output with `pytest`.