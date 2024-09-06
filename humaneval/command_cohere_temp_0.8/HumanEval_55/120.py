```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python function uses a recursive approach to calculate the Fibonacci sequence, which is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. Here's how it works:
1. The function first checks if the input `n` is less than 2. If so, it returns `n` itself since the first two numbers in the Fibonacci sequence are 0 and 1.
2. If `n` is greater than or equal to 2, the function uses recursion to calculate the nth Fibonacci number by summing the (n-1)th and (n-2)th Fibonacci numbers. 

This approach leverages the fact that the Fibonacci sequence has a recursive relationship, making it efficient to calculate larger Fibonacci numbers from smaller ones. However, due to the exponential growth of the sequence, this method becomes less efficient for very large n, requiring billions of steps to compute the Fibonacci number. But for small to moderate values of n, like in the test cases provided, this recursive approach is efficient and convenient.