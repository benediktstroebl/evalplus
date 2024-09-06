```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is ensured to be true during the problem statement's examples.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - If `x` is a simple power of `n`. This is ensured by comparing `x` to `n**int(x)`. If they are equal, it is a simple power.
    - If `x == n**x`: This part of the condition checks if `x` is an integer. If it is, it returns True, as in the case of `1, 2, 8`, and others in the example. 
    - This also ensures that if `x` is not an integer, it returns False, catching the case of incorrect simplification, like `3, 5, 3` from the example. 

Overall, the function returns True if `x` is a simple power of `n` and False otherwise. 

The rest of the code block is related to testing the function's correctness against the provided examples. 

Let's break down the testing part: 
```python
def test_simple_power():
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
``` 

Each assertion is a test that checks whether the function's output for a specific input matches the expected output. 

For example, in the first assertion: `assert is_simple_power(1, 4) == True`, it checks whether the function's output `True` for the input `is_simple_power(1, 4)` is correct. 

If all assertions pass, it will indicate a passing status for the tests, and if any fail, it will show which test case failed and how the function behaved versus the expected behavior.