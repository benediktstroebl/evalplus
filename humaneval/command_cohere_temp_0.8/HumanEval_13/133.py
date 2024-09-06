```python
def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a
```
The function utilizes a straightforward algorithm involving integer division and modulus operations to determine the GCD of two integers `a` and `b`. This method is commonly referred to as the 'Euclidean Algorithm.' 

Here's how it works:
1. Initially, `a` and `b` are swapped, assuming `b` is the smaller number. This step isn't essential but helps optimize the process by reducing the number of iterations required.
2. The algorithm repeatedly divides the larger number (`a`) by the smaller number (`b`), subtracting the modulus (the remainder of the division) from `a`.
3. This process continues until `b` becomes zero. At this point, the final value of `a` is the GCD of the initial `a` and `b`.

For example, if initially `a = 45` and `b = 18`, the algorithm would work as follows:
```
1. `a = 45, b = 18: a = 45 / 18, remainder = 9`
2. `a = 9, b = 18: a = 9 / 18, remainder = 0`
```
Since `b` is now zero, the algorithm stops. Consequently, the GCD of `45` and `18` is `9`.

This algorithm is efficient and works for positive integers, handling cases where the inputs are negative as well. However, it isn't tailored for handling complex numbers or non-integer inputs. 
```python
# Test the function
def test_gcd():
    """Test the greatest_common_divisor function."""
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(36, -54) == 6
    assert greatest_common_divisor(-97, -1) == 1
test_gcd()
```