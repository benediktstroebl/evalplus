```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and the product of the signs and returns the sum of the magnitudes multiplied by the product of the signs.

Here is a breakdown of the steps taken by the function:
1. The function first checks if the array is empty, and returns None if it is.
2. Using list comprehensions, it separately calculates the magnitudes and signs of elements in the array. 'abs()' is used to obtain the magnitudes of each integer, and a list comprehension checks if each integer is positive, negative, or zero, and assigns 1, -1, or 0, respectively, as the sign.
3. The function then calculates the sum of the magnitudes and the product of the signs using the `sum()` and `prod()` functions respectively.
4. Finally, it returns the result of the multiplication of the sum of magnitudes and the product of signs. 

This solution is efficient and can handle any array, regardless of its size or content. 
```python
assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) == None
```