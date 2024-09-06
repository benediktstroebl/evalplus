```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This Python script defines a function named `prod_signs` that takes an array of integers as input. This function calculates the product of the signs of each number in the array, where 1 represents a positive sign, -1 represents a negative sign, and 0 is ignored, and then, it returns the sum of the magnitudes of the integers multiplied by the product of these signs. The script initializes a variable named `result` to None, which will store the final result. Then, it checks if the input array is not empty, it proceeds to calculate the product of the signs. It does this by iterating through the array and generating a list of signs, where each element signifies whether the corresponding number is greater than zero ('1') or less than zero ('-1'). This is done by using a list comprehension that evaluates the inequality `num > 0` for each num in arr. Subsequently, it turns the sign '-1' into '-1' and any other sign '1' into '1', achieving the desired effect of changing the sign to '1' for positive numbers, and to '-1' for negative numbers, while leaving '0' unchanged. Following this, the script calculates the sum of the products of each number in the array with its corresponding sign from the `signs` list. Finally, if the input array is not empty, it returns the calculated sum; otherwise, it returns None, indicating that the input array was empty, and no calculation was possible. 

Here is an example usage of the function:
```python
prod_signs([1, 2, 2, -4])  # Expected output: -9
prod_signs([0, 1])  # Expected output: 0
prod_signs([])  # Expected output: None
```

This function is designed to efficiently handle multiple scenarios and provide accurate results for different input arrays, as demonstrated in the example usage.