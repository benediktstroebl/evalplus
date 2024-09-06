Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reversed_sorted_arr:
        if num <= 9:
            result.append(str(num)[-1])
            result.append('Zero' if num == 0 else 'Nine' if num == 9 else '')
    return result
```

The `by_length` function first sorts the array with the lambda function, which sorts numbers between 1 and 9 inclusive, and float('inf') otherwise. The resulting array is then reversed and iterated through to store the named digits and empty strings between them. The given test cases should prove the functionality of the function with this code block.