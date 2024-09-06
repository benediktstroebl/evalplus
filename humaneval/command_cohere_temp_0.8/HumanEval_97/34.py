```python
def multiply(a, b):
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by accessing the last character in their string representations (`str(a)[-1]` and `str(b)[-1]`). It then multiplies these last digits, converting the result back to an integer using `int()`, and returns the final answer. 

Here is an example usage of the function:
```python
print(multiply(12, 3))
```
This would output:
```
3
```

This reflects the problem statement's requirement that the function returns the product of the unit digits of 12 and 3, which is 3. 

Such a straightforward approach highlights the importance of understanding the problem thoroughly before diving into a solution.