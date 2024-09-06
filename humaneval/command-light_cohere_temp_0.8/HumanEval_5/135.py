Here is a self-contained Python script that solves the problem of inserting a number `delimiter` between every two consecutive elements in the input list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result
```

This function takes two parameters: `numbers`, which is the input list of numbers, and `delimiter`, which is the number to insert between each pair of consecutive elements. The function then iterates through the list, and checks if the current index `i` is even or odd. If it's odd, the number at index `i` is appended to the `result` list with an additional `delimiter` value. If it's oses the a number is added to the list, and the process is repeated until the entire list has been processed.