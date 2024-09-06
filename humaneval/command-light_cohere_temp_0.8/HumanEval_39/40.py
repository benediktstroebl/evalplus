Here's a self-contained Python function that computes and returns the n-th Fibonacci number that is also prime:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    temp = prime_fib(n // 2)
    if temp == 0:
        return 0
    return temp + (prime_fib(n % 2) != 0)
```
This function uses a simple recursive approach to find the n-th Fibonacci number that is prime. It first handles base cases for n=1,2,3, then checks for divisibility by 2 and 3, returning 0 in such cases. If the result for the certain number is 0, then it is not a prime, otherwise, the result is the sum of two prime Fibonacci numbers.