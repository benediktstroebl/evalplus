Here's a self-contained Python function that solves the problem of inserting a delimiter between every other element in a list:
```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for num in numbers:
        result.append(num)
        result.insert(delimeter, result[0])
    return result
```
This code defines a function called `intersperse` that takes in a list of integers `numbers` and an integer `delimeter` as input. The function iterates through the process to insert `delimeter` after the first element of the list and then append the remaining elements of the list to a new list.