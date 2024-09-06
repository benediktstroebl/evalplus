```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The GCD method uses Euclid's algorithm iterative approach to find the highest integer that divides both numbers evenly. It utilizes the fact that the GCD of two numbers 'a' and 'b' is the same as the GCD of 'b' and 'a% b'. When 'b' is 0, the loop terminates and the GCD is 'a'.