Here is a Python script with a self-contained function that solves the problem of inserting a number `delimiter` between every two consecutive elements of the input list:

```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i] + delimiter + numbers[i+1])
        else:
            result.append(numbers[i])
    return result

# Example usage
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and a `delimiter` as input and returns a new list with the elements interspaced. The function works by iterating through the list, appending the current element to the result list with a specified `delimiter` if there are more elements to come, otherwise, append the current element to the result list.