Here's the provided Python script:
```python
def any_int(x, y, z):
    return (x == y + z) and (type(x) == int and type(y) == int and type(z) == int)

x = any_int(5, 2, 7)  # True
y = any_int(3, 2, 2)  # False
z = any_int(3, -2, 1)  # True

# Test types of the function with a complex example
print(any_int(3.6, -2.2, 2))  # True
```

This script defines a function **`any_int`** that checks if a given set of numbers meets a specific condition: all the numbers must be integers, and one of them must be equal to the sum of the other. The function returns **`True`** if the condition is met and **`False`** otherwise. It passes the test all three variables are of integer type, and the condition is met.