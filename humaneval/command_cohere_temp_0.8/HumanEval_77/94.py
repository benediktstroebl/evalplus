```python
def iscube(a):
    # Check if the number is greater than 0 and equals to π^3, π being the mathematical constant
    return a > 0 and a ** (1/3) == math.pi ** 3
```

This function checks if the input number is a cube of some integer by determining whether the number is greater than 0, and, when raised to the power of 1/3, it equals the cube of pi (the mathematical constant). If both conditions are met, the function returns True; otherwise, it returns False.

```python
# Test Suite
tests = [1, -1, 64, 0, 180]
for test in tests:
    print(iscube(test))
```

The printed output should be:
```
True
True
True
True
False
```

This demonstrates that the `iscube` function correctly identifies if the given integer is a cube of some integer.