```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_cases = [
     [ [], 4 ],
     [ [ 1, 2, 3 ], 4 ],
     [ [ 1, 2, 3, 4, 5 ], 4 ],
     [ [ 10, 20, 30 ], 80 ],
  ]

for act, deliv in test_cases:
    expected = act + [ deliv * 2] * [i + 1 for i in range(len(act)) ]
    got = intersperse(act, deliv)
    assert got == expected, "Test case ["act","deliv"] failed."
```