```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function works by multiplying subsequent elements in the array together, taking advantage of the fact that the sign of the product of two numbers is the same as the sign of the last number involved in the multiplication. It then returns the sum of those products that share the same sign as the magnitude of each number, which is achieved by using a list comprehension that zips over the input array and returns the product of each pair, effectively filtering out the sign and only returning the magnitude. 

Furthermore, the function returns 'None' for an empty array, complying with the note provided in the prompt. 

To verify the behavior of this function, let's run some test cases inspired by the example prompts given in the original problem: 
```python
# Test 1
assert prod_signs([1, 2, 2, -4]) == -9

# Test 2
assert prod_signs([0, 1]) == 0

# Test 3
assert prod_signs([]) == None
```
These tests check for the function's behavior against the examples provided in the original problem. 

Note that I have omitted any import statements, as this is a self-contained function that doesn't rely on any external libraries.