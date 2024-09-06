```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        result.append(numbers[i] + delimeter) if i < len(numbers) - 1 else numbers[i]
    return result
# Test the function with different inputs
test_cases = [
    [], 4
    [1, 2, 3], 4
    [1, 2, 3], 5
    [10, 20, 30], 1  # New line between 20 and 30
]
    [10, 20, 30], 40  # New line between 20 and 40
]

for tc, test in enumerate(test_cases, start=1):
    actual = intersperse(test, 10)
    expected = [11, 21, 31]
    print(f"Test {tc}: {actual} != {expected}")
    if actual != expected:
        print("Failed")
    else:
        print("Passed")
```  The code defines a function called `intersperse` that takes a list of numbers and a delimiter as input, and it returns a new list with numbers separated by the delimiter. The function uses a loop to iterate through the input list, appending the next number with the current delimiter to the result list if the current element is not the last element, otherwise, it adds the current element to the result list. The output is then compared to a list of test cases, and it prints whether the function passed or failed the test.