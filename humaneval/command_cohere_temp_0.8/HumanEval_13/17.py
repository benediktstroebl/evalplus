```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm works by the Euclidean algorithm idea of continually using the formula:
```
GCD(a, b) = GCD(b, a % b)
```
The base case of this recursive approach is when b == 0, where the GCD is then effectively a. The Euclidean algorithm is efficient and finds the GCD in O(log(min(a, b))).

Here is a test suite that you can use to verify the functionality of the code:
```python
def test_gcd():
    """ Tests the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 45) == 45
    assert greatest_common_divisor(100, 25) == 25

test_gcd()
```
Run this test suite to confirm that the implementation behaves correctly.  This will validate the GCD algorithm, and ensure that the function returns the correct value for the given inputs. 
The `assert` checks the expected result against the actual result from the function. If the assertion passes, it confirms that the function returns the expected output.