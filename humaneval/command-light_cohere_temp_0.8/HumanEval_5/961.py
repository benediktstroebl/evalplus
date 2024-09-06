Here is a self-contained Python function that solves the problem of inserting a specified delimiter between every two consecutive elements in a list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:  # Only insert the delimiter if it's not the first element of an even-length sequence
            result.append(delimeter)
        else:
            result.append(numbers[i])
    return result
```
This function takes a list of integers `numbers` and an integer `delimeter` as input and returns a new list with the elements of `numbers` separated by the `delimiter`. 

The function uses a list comprehension and a conditional to iterate through the list and determines whether to insert the `delimiter` or to append the current element of the list.