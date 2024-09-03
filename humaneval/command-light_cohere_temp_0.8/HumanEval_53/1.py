```python
def add(x: int, y: int):
    return x + y

for i in range(10):
    if not(add(i, 10) == 10):
        print("add function is incorrect")
    else:
        print("add function works correctly")
```