```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    for i in range(2, n + 1):
        result //= factorial(i)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Tests
def test_special_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288

test_special_factorial()
```

This code defines the `special_factorial` function, which calculates the "Brazilian factorial" as described in the prompt. It iterates through the numbers from 1 to `n` and accumulates the result, then iterates again to remove the factorials of all numbers between 2 and `n` from the result. The `factorial` function is also defined to assist in the calculation. Finally, the code includes a test suite, `test_special_factorial`, to validate the correctness of the `special_factorial` function with a few example inputs. 

To run the code, save it in a `.py` file (e.g., `brazilian_factorial.py`) and execute it using a Python interpreter. The script is self-contained and does not rely on external modules or dependencies, making it portable and easy to execute.