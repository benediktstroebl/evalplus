```python
def multiply(a, b):
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers as input and extracts the last digit of each number using `str(a)[-1]` and `str(b)[-1]`. It then multiplies these extracted digits using `int()`, ensuring they are also treated as integers. The result of this multiplication is then returned, completing the task of finding the product of the unit digits of the two input numbers. This method is adaptable and provides an elegant solution to the problem at hand.

Here is an example usage of the function:
```python
print(multiply(12, 4))
```
This will print out the expected output of the function, which is **4**.