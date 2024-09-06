Here is a self-contained Python script that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [num / max(numbers) for num in numbers]
    return [min(numbers) for _ in range(max(numbers))] + [max(numbers) for _ in range(max(numbers))]

test_list = [1.0, 2.0, 3.0, 4.0, 0.0, 0.5]
print(rescale_to_unit(test_list)) == [0.0, 0.0, 0.0, 0.5])
print(rescale_to_unit([1.0, 3.0, 4.0, 0]) == [0.0, 0.0, 0.0, 0])
print(rescale_to_unit([2.0, 0, 3.0, 0]) == [0.0, 0.0, 0.0, 1.0])
print(rescale_to_unit([0.0, 0, 2.0, 3.0]) == [0.0, 0.0, 1.0])
print(rescale_to_unit([0.0, 0, 2.0, 3.0]) == [0.0, 0.0, 0)
```