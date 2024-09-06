```python
def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

def test_fib4():
    n = 7
    assert fib4(n) == 14  # Fibonacci number at position n

if __name__ == "__main__":
    test_fib4()
```
The script defines the function `fib4` which computes the n-th Fibonacci number in the Fibonacci sequence using the formula: `F(n) = F(n-1) + F(n-2) + F(n-3) + F(n-4)`. 

The `test_fib4` function is used to test the `fib4` function, passing the value `n` as an argument and asserting that the result is the Fibonacci number at that position.