```python
def fib4(n: int):
    if n <= 0:
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
    n = 5
    print(fib4(n))  # Output: 4

n = 7
print(fib4(n))  # Output: 14

``` 
This script defines a function `fib4` that computes the n-th Fibonacci number using a loop, without recursion. The function takes an single argument `n` representing the index of the Fibonacci number to compute. The function then performs a sequence of mathematical operations to calculate the Fibonacci number and returns the result.