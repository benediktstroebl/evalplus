```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by accessing the last element of their string representations using `str(a)[-1]` and `str(b)[-1]`. This is achieved using `int( )` to convert the string to an integer without converting the last digit to an integer. These extracted last digits are then multiplied and returned as the result. 

Here is an example usage of the function:
```python
print(multiply(12, 4))
```
This will print out the product of the unit digits, resulting in 4. 

This approach is concise and achieves the goal using EAFP principles with an emphasis on using string manipulation and integer casting.