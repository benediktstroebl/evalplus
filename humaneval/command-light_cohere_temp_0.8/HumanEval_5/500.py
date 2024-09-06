Here is a self-contained Python script that solves the problem of inserting a number 'delimiter' between every two consecutive elements of a given list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        while len(result) > 1 and numbers[i] == numbers[result[-1]]:
            result.append(delimiter)
        result.append(numbers[i])
    result.append(delimiter)
    result.append(numbers[i+1])
    return result
```

This function takes a list of integers `numbers` and an integer `delimiter` as input, and returns a new list with the elements of the original list interspersed with the specified `delimiter`. The function uses a loop to iterate through the input list and adds the `delimiter` between every two consecutive elements if the current element is not equal to the element immediately before it in the `result` list.