```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        product_of_signs = prod(signs)
        result = sum(magnitudes) * product_of_signs
    return result
```
The `prod_signs` function takes an array of integers (`arr`) as input. It calculates the product of signs of each number in the array using the `prod` function and sums the magnitudes of the integers using a list comprehension. Then, the result is computed by multiplying the sum of magnitudes with the product of signs. If the input array is empty, it returns `None`.

The `prod` function calculates the product of the list of numbers. It combines all the values in the list by multiplying them together, handling positive and negative numbers correctly.

This solution adheres to the problem statement by considering the signs of the integers and calculating the correct product of signs, while also handling an empty input array appropriately.