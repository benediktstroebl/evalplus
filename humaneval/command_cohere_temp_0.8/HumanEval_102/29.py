```python
def choose_num(x, y):
    max_even = -1
    temp = x
    while temp <= y:
        if temp % 2 == 0:
            max_even = temp
        temp += 1
    return max_even
```

The function searches for even numbers between x and y and uses a while loop to do so. It ensures that the code correctly returns -1 if no even number exists within the range. You can verify this behavior with the following tests:
```python
> choose_num(12, 15)
14
> choose_num(13, 12)
-1
``` 
The provided code is a clear and efficient way to tackle the problem.