```python
def prod_signs(arr):
    result = None
    if arr:
        arr = [abs(x) for x in arr]
        arr = [x * y for x, y in zip(arr, [1, -1])]
        result = sum(arr)
    return result
```
This function follows the specification closely. It first filters out the absolute values of the integers using a list comprehension. Then, it multiplies each element in the list by a corresponding sign vector [1, -1] using zip and a multiplication operation. Finally, it sums the resulting list to obtain the final result. The initial result is set to None for an empty array, as specified in the problem statement.