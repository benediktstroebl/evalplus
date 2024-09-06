```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result
```
Here, the `intersperse` function takes a list of integers `numbers` and a delimiter `delimeter` as input. It uses a permanent variables to store the last number and the current number in the for loop, which allows it to separate every other pair of numbers with the specified `delimiter`.