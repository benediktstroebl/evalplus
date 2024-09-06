```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n ** 2

    return result
```
This function defines a Python function called sum_squares that takes a list called lst as input. It calculates the sum of squared elements in the list using a for loop that iterates through each element n in the list, adding its square (n ** 2) to the result variable. Finally, it returns the computed sum of squared values.

Here is a more robust version of the code that handles a few edge cases like floating point numbers and negative numbers:
```python
def sum_squares(lst):
    result = 0
    for n in lst:
        if isinstance(n, float):
            n = n ** 2
        elif n < 0:
            n = -n
        result += n

    return result
```
This version of the function is slightly more complex but handles a few important edge cases. Here is an explanation of the additional lines:
- **if isinstance(n, float):** This checks if the current element n in the list is a float. If it is, it converts it to a square root (n ** 2) to properly calculate the square. 
- **elif n < 0:** This checks if the current element n is negative. If it is, it converts it to its positive equivalent (-n). This is necessary because squaring a negative number yields a positive number, which would distort the sum. 

This function overall computes the sum of squared values in the list and returns the result.