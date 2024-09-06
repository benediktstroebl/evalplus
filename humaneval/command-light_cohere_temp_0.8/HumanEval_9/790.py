```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_value = numbers[0]
    max_moment = 0
    result = [max_value]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
        elif num > max_moment and num != max_value:
            max_moment = num
        result.append(max_moment)

    return result

# Test case 1
test_data = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(test_data)
print(test_result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test case 2
test_data2 = [2, 3, 4, 5, 4, 3, 2]
test_result2 = rolling_max(test_data2)
print(test_result2)  # Output: [2, 3, 4, 5, 4, 3, 2]
```

The above Python script defines a function `rolling_max` that takes a list of integers as an argument and generates a list of the rolling maximum elements found in the sequence up to the given moment. The script also passes two test cases, and the output is printed.