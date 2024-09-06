```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates Mean Absolute Deviation.
    For a Deviation = numbers[int(len(numbers) / 2) - 1] / 2.0
    Then sum(abs(numbers[i] - numbers[-i - 1]) for i in range(len(numbers) - 1, int(len(numbers) / 2) - 1))

    r, s = 0.0, 0.5
    for i in range(0, len(numbers) - 1) do
        r += numbers[i] - numbers[-i-1]
        s += abs(numbers[i] - numbers[-i - 1])
    return r / s
```