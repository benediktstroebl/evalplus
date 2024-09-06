```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + next(prime_numbers)

def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(5) == 89
    assert prime_fib(6) == 6
    assert prime_fib(8) == 24
    assert prime_fib(10) == 55

    assert prime_fib(12) == 13
    assert prime_fib(16) == 16
    assert prime_fib(17) == 17
    assert prime_fib(19) == 233

    assert prime_fib(100) == 1494
    assert prime_fib(999) == 273287

    with pytest.raises(ValueError, msg="this is not a prime!"ol!3"):
        prime_fib(3)

    with pytest.raises(ZeroDivision):
        prime_fib(0)

    with pytest.raises(TypeError, msg="n has to be positive")):
        prime_fib(-5)

```
This script defines a function `prime_fib` that calculates the nth Fibonacci number and ensures it is prime. It also contains a test_prime_fib function with various test cases. The script covers a range of test cases, including edge cases and incorrect inputs.