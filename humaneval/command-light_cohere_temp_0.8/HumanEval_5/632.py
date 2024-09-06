Here's the Python script with a self-contained function that solves the problem of inserting a number `delimiter` between every two consecutive elements of an input list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]) + delimeter
        else:
            result.append(numbers[i])
    return result
```
This function takes a list of integers `numbers` and a delimiter integer `delimeter` as input. It uses a scenario-specific logic to return a new list with the elements of the input list interspaced by the `delimiter`.