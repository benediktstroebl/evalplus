Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function first checks if `n` is less than 2, returning `False` if so. It then iterates from 2 up to the square root of `n` (inclusive), checking whether `n` is divisible by any of these numbers. If any such divisor is found, the function returns `False`. However, if no divisors are found, the function returns `True`, indicating that `n` is a prime number. This approach ensures efficiency by eliminating the need to check unnecessary factors past the square root of the number. 
The test cases provided in the prompt aim to demonstrate the behavior of the function on both prime and non-prime numbers, and the function's output aligns with each test case's expected outcome. Picking a good set of test cases is crucial for reliable testing, and usually, it's recommended to use various numbers to cover a wide range of scenarios, including the edge cases (like small numbers, large numbers, odd numbers, etc.). 
You can use these test cases to further verify that the provided solution is correct. 

```python
# Test the is_prime function
def test_is_prime():
    assert is_prime(101) == True
    assert is_prime(11) == True
    assert is_prime(13441) == True
    assert is_prime(61) == True

    assert is_prime(6) == False
    assert is_prime(4) == False
    assert is_prime(1) == False
```
The test cases in the code above cover a range of scenarios, from known prime numbers to known non-prime numbers. 
The `assert` statements verify that the function's output aligns with the expected truth values. 
If all the assertions pass, it indicates that the function implementation is correct and aligns with the given test cases. If any of the assertions fail, it indicates that the function's behavior doesn't match the expected outcomes, prompting further investigation into the code's correctness. 
Overall, this script provides a standalone function that solves the problem and incorporates testing functionality to verify correctness against a range of inputs.  Any number of additional test cases could be added to further enhance the testing scope, but typically it's important to focus on a representative set of test cases that cover the range of possible inputs, rather than trying to test every single number (which is virtually impossible for very large numbers).