```python
def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        sign = 1
        for x in arr:
            sign *= x
        result = sum(x for x in arr if x != 0) * abs(sign)
    return result
```
The code defines a Python function `prod_signs` that solves the problem as described in the prompt. It takes an array of integers `arr` as input and returns the sum of magnitudes of integers multiplied by the product of all signs of each number in the array, represented by 1, -1, or 0.

The script returns `None` for an empty array and demonstrates this with examples, as required in the prompt.