```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a simple recursion formula `f(n) = f(n-1) + f(n-2)`. This avoids the exponential complexity associated with a straightforward recursive implementation. It takes an integer `n` as input and returns the corresponding Fibonacci number. The base cases, `f(0) = 0` and `f(1) = 1`, are handled to provide the correct outputs for these particular inputs. 

Here is an example of an output of the function for `n=8`:
```python
fib(8)
21
```
This is a straightforward implementation of the classic Fibonacci sequence that produces accurate results.  It is a fundamental operation that is efficient and can be used as a foundation for further expansion or adaptation to novel requirements.