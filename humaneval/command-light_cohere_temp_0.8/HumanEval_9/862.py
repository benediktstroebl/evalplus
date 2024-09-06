Here's the solution to the problem:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, _ in sorted(enumer(), key=lambda x: x[1]) if n > max_: max_ = n]

# Test cases
numbers1 = [1, 2, 3, 2, 3]
numbers2 = [1, 2, 3, 4, 5]
numbers3 = [1, 2, 2, 3, 3, 4, 5, 6]

print(rolling_max(numbers1))  # Expected output: [1, 2, 3, 3, 3, 4, 4]
print(rolling_max(numbers2))  # Expected output: [1, 2, 3, 4, 4]
print(rolling_max(numbers3))  # Expected output: [1, 2, 3, 3, 3, 4, 5]
```

Please ensure that you have the `typing` library installed. You can install it convenient with:

```bash
pip install typing
```