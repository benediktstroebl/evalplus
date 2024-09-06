```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the input array and combines it with the product of signs of each number to return the desired result. If the input array is empty, it returns `None`. Feel free to test it with the examples provided or any other scenarios you want to explore!