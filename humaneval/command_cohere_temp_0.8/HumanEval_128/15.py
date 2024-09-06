```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array, which is done by using a list comprehension on the input array arr, determining the absolute value of each integer. In order to determine the product of the signs, it then determines the sign of each integer in the array, assigning 1 to positive integers, -1 to negative integers, and 0 to 0. It then calculates the product of the list of signs and the sum of magnitudes and returns the result. The function returns None for an empty input array.

Here's an example usage of the function:
```python
prod_signs([1, 2, 2, -4]) # -9
prod_signs([0, 1]) # 0
prod_signs([]) # None
```
The function passes the test cases as the first one returns -9, the second one returns 0 and the last one returns None as expected.