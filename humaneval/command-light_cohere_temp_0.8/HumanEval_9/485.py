```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num >= 0]  # Remove negative numbers to ensure correct behavior
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]
test_cases = [
    [1, 2, 3],
    [2, 3, 4, 2],
    [3, 2, 1, 3, 4],
    [-1, 2, 3, 4, 5],
    [100, 101, 102]
]

results = []
for test_case in test_cases:
    results.append(rolling_max(test_case))

for r in results:
    assert len(r) == 1, f"Wrong result. The correct result should be a list of one number:
    assert r[0] == max(test_case), f"Wrong result: {r}"
 ```
Do you want me to assist you in solving problems or coding related to other topics?