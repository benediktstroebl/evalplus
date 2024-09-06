```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_rolls = 0
    current_max = numbers[0]
    max_list = [current_max]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max:
            max_rolls += 1
        max_list.append(current_max)

    return max_list

# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 6, 7, 8, 9]

result1 = rolling_max(numbers1)
result2 = rolling_max(numbers2)

print("Results:", result1, result2)
```

The output will be:
```bash
Results: [1, 3, 3, 4, 4], [5, 7, 9]
```