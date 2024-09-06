```python
def greatest_common_divisor(a, b): 
    while b != 0:
        d = b
        b = a % b 
    return d

# Test case 1
assert greatest_common_divisor(3, 5) == 1

# Test case 2
assert greatest_common_divisor(25, 15) == 5

# Test case 3
try:
    print(greatest_common_divisor(-5))
except AssertionError:
    print('Did not give me a number')

# Test case 4
try:
    print(greatest_common_divisor(1))
except AssertionError:
    print('Did not give me a number')

# Test case 5
try:
    print(greatest_common_divisor(15, 7))
except AssertionError:
    print('Don''t have this number')
```