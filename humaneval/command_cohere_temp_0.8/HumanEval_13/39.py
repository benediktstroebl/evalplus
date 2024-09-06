```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The algorithm is a continuation of the Euclidean algorithm, specifically the latter part of it where the GCD is computed iteratively. It's more of a trade-off between space and time complexity as it only uses a single variable whereas the more common approach with modules is more space-efficient.

Here is a test suite for the function:
```python
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(121, 43) == 17
    assert greatest_common_divisor(121, 0) == 121

test_gcd()
``` 
The test suite will assert the function behaves as expected. 

This approach uses a single variable to keep track of the interim GCD, which trades off space efficiency for time efficiency as compared to the more common approach using modules.  While this approach uses more iterations than the module approach, it uses constant space which could be beneficial if space efficiency is more important in your use case.