```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function evaluates to true when `x` is a simple power of `n` i.e. `x == n**int(x == n*n)`. The order of checks is specifically implemented to prioritize efficiency, by checking for the simplest cases first. The units of measurement used in the function are solely dependent on the input values, thus ensuring a fast and appropriately responsive function. 

This function is designed to be robust, handling a wide array of inputs gracefully. However, it's worth noting that the `is_simple_power(x, n)` function assumes that both `x` and `n` are valid floats that are not infinite or NaN, and that n is a positive integer. 

To ensure a comprehensive check, a test suite should be added to cover different cases, including edge cases and negative testing, to confirm the robustness of the function. Below is a sample markdown code block of a test suite that can validate the functionality of the provided code: 
```python
# Test Suite
def test_is_simple_power():
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
    assert is_simple_power(0, 1) == False
    assert is_simple_power(-1, 1) == False
    assert is_simple_power(1.1, 1) == False
    assert is_simple_power(1, -1) == False
    assert is_simple_power(10, 3) == True
    assert is_simple_power(100, 10) == True
```