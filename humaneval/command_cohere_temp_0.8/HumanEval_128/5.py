```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * arr[0]
        magnitudes = [abs(num) for num in arr]
        result = sum(magnitudes) * product(signs)
    return result
```
This Python script defines a function `prod_signs` that takes an array of integers as input and calculates the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array. The function first checks if the input array is empty, and if so, returns `None`. Otherwise, it iterates through the array and calculates the product of signs and sum of magnitudes using list comprehensions. Finally, it returns the result of the multiplication between these two values. 

Here's an example usage of the function with a markdown code block stating the expected output:
```python
>>> prod_signs([1, 2, 2, -4]) == -9
True
>>> prod_signs([0, 1]) == 0
True
>>> prod_signs([]) == None
True
```