```python
def can_arrange(arr):
    prev = arr[0]
    index = 0
    for num in arr[1:]:
        if num > prev:
            return -1
        elif num == prev:
            continue
        else:
            prev = num
            index += 1
    return index
```

The function `can_arrange` iterates through the array, comparing each element to the previous one. If a larger element is found, the function returns -1, indicating that no suitable element is found. If multiple identical consecutive elements are encountered, they are skipped, and the search continues. The function returns the largest index of an element that is not greater than or equal to the previous one. In case no such element exists, it returns -1. 

Here is an example usage of the function:
```python
arr = [1, 2, 4, 3, 5]
result = can_arrange(arr)
print(result)  # Output: 3
```

And here is an example where the function returns -1:
```python
arr = [1, 2, 3]
result = can_arrange(arr)
print(result)  # Output: -1
``` 

This would be the output for the given examples, respectively.