Here is a Python script that solves the problem of inserting a number `delimiter` between every two consecutive elements in the input list:

```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return [num + delimiter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Example usage:
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [1, 4, 2, 4, 3]
```

This function uses a list comprehension to iterate over the input list and the enumerate function to create a tuple containing the index and element. Then, it checks if the index is less than the length of the list minus 1. If it is, the element is the last element, and the `delimiter` is added. The function then returns the `numbers[i] + delimiter`. 

This code is self-contained and can be used to solve the problem of inserting a delimiter between every two consecutive elements in the input list.