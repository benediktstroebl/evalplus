```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]

rolling_max_test_1 = [1, 2, 3, 2, 3, 4]
rolling_max_test_2 = [5, 1, 6, 4, 7]
rolling_max_test_3 = [10, 2, 3, 4, 2]

result_1 = rolling_max(rolling_max_test_1)
result_2 = rolling_max(rolling_max_test_2)
result_3 = rolling_max(rolling_max_test_3)

print(f"Result for test 1: {dictionary}")
print(f"Result for test 2: {dictionary}")
print(f"Result for test 3: {dictionary}")

for result, test in zip([result_1, result_2, result_3], [rolling_max_test_1, rolling_max_test_2, rolling_max_test_3])):
    print(f"{test}: {list}")
    print(f"{result}: {max_num}")
```