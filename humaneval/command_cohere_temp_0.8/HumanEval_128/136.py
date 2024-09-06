```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(x) for x in arr) * product(x % 2 for x in arr)
    return result
```
The `prod_signs` function takes an array `arr` as an argument and returns the sum of magnitudes of integers multiplied by product of all signs of each number in the array. The function checks if the array is empty, and returns `None` if so. Otherwise, it uses two generators: one to calculate the sum of magnitudes and one to calculate the product of signs. Both generators are list comprehensions with lambda expressions as their filters. When iterated over these generators for each number in the array, the product of all signs and the sum of magnitudes are calculated.