```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list."""
    res = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            res.append(numbers[i] + delimeter)
        else:
            res.append(numbers[i])
    return res
```
This Python function `intersperse` takes a list of integers `numbers` and a delimiter `delimeter` as input. The function iterates through the list and adds the `delimiter` between every two consecutive elements if the index is divisible by 2 (even index), otherwise, it adds the element to the list.

The function is well-contained, and it efficiently solves the problem of inserting a delimiter between every two consecutive elements in the input list.