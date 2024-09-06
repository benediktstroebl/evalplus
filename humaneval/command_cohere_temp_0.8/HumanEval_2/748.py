```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` (the integer part of the decomposition described in the prompt). The result is the residual fraction (also known as the decimal part), which is less than 1. 

This approach follows the principles of basic arithmetic and integer operations in Python:
1. `number` = 3.5, `int(number)` = 3 (the largest integer less than 3.5)
2. `3.5 - 3` = 0.5 
3. The residual fraction is indeed the decimal part of the number, which is less than 1. 

Thus the function correctly returns the decimal part of the number, in accordance with the prompt's instructions. 

The function is also self-contained, meaning it does not rely on any external variables, and needs no imports. It is a simple definition-body function that can be invoked and tested directly within the Python environment, making it fully self-contained within a single script.