```python
def greatest_common_divisor(a, b): 
    while b != 0:
        b, a = a % b, b
    return a

# Test case 1
assert greatest_common_divisor(3, 5) == 1

# Test case 2
assert greatest_common_divisor(25, 15) == 5

# Test case 3
try:
    print(greatest_common_divisor(-5))
except AssertionError:
    print("Attempt to find a common divisor of a negative number.")
```