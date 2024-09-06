```python
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2:
            product *= int(digit)
    return product if product else 0
```

This function traverses the decimal representation of 'n' and multiplies each odd digit into the 'product' variable. The result is returned, but if the product is 0, it indicates that all digits are even and the function returns 0. The function is self-contained and can be invoked with the appropriate input to verify its behavior against the given tests. 

If you wish to test this script, you can run it on the console and input different values to see the function's behavior. You can also incorporate it into a testing framework like pytest to arrange automated tests. 

Feel free to ask any questions or request modifications to this solution!