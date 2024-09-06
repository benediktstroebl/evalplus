Here's a self-contained Python function that solves the problem of inserting a number 'delimiter' between every two consecutive elements of a list:
```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i] + delimiter)
        else:
            result.append(numbers[i])
    return result
```
This script defines a function '**`intersperse`**' that takes a list of integers '**`numbers`**' and a '**`delimiter`**' as input. It then iterates through elements of the list and, for each element, appends the current element and the '**`delimiter`**' to the result list if there's a subsequent element, and appends the current element to the result list otherwise.