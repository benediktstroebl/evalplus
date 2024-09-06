Here is a self-contained Python function that calculates the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a, b):
    if not divisible(a, b):
        return 0

    d = a
    while b != 0:
        a, b = b, a % b
    return d

def divisible(x, y):
    return x > 0 and y > 0 and x % y == 0

# test_divisor
def test_divisor(test_value):
    assert greatest_common_divisor(test_value, 10) == 5

test_values = [3, 5,25,15]
for test_value in test_values:
    print(f'Test {test_value}: {test_divisor(test_value, 10)}')
```

This function `greatest_common_divisor` takes two integers a and b as parameters and calculates their greatest common divisor using a `divisible` helper function. The `divisible` function checks if both `x` and `y` are positive and if `x` divides `y` without leaving a remainder. 

The `greatest_common_divisor` function then iterates through each potential divisors of `b` while keeping track of the greatest divisor `d` until it reaches a value of `a` that is no longer divisible by `b`.  This allows the function to efficiently find the greatest common divisor.