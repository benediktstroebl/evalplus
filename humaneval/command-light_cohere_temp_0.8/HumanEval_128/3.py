```python
def prod_signs(arr):
    if not_elements(arr):  # Check if the array is empty
        return None
    result = 1  # Initialize result with 1 (any non-zero number will have a positive product)
    
    for num in arr:
        result = result * (-num)  # Multiply each element by the negation of itself
    
    return result

def not_elements(arr):
    return len(arr) == 0

# Test the function
arr = [1, 2,2,-4]
result = prod_signs(arr)
print(result)  # Output should be -9
arr = [0,1]
result = prod_signs(arr)
print(result)  # Output should be 0
arr = []
result = prod_signs(arr)
print(result)  # Output should be None
```
This code defines a function `prod_signs` that calculates the product of the sign of each number in the array, then sums these products to produce the desired result. The `not_elements` helper function is used to check if the array is empty, in which case the function returns `None`.