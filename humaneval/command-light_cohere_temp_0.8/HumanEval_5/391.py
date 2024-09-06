Here's a solution to your problem:

```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    numbers = list(numbers)  # Convert input list to mutable Python list
    result = [num for num in numbers if num != delimeter] + [delimeter] + [num for num in numbers if num != delimeter]
    return result
```

This function takes two parameters: `numbers`, which is a list of integers, and `delimeter`, which is an integer. It uses a process to create a new list by concatenating elements that are not `delimeter` with a space, followed by `delimeter` and the rest of the elements that are not `delimeter`. 

The function then returns this new list, which effectively "intersperse"s the `delimeter` between every other two elements in the input list.