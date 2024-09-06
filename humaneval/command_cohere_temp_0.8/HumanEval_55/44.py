```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
This Python script defines a function called fib, which takes an integer n as input. It returns the n-th Fibonacci number. The base cases are handled with the condition `if n < 2:`, where if `n` is 1, it returns 1, and if `n` is 0, it returns 0. For any other value of `n`, the function recursively calls itself with the arguments `n-1` and `n-2` and returns the sum of the results of these recursive calls, which will be the next Fibonacci number. This recursive approach is more efficient than the naive linear approach that calculates Fibonacci numbers based on the Fibonacci sequence's mathematical definition. 
The function's behavior is demonstrated by the tests provided in the prompt, as it correctly returns the 55th Fibonacci number when given a input of 10, returns 1 when given a input of 1, and returns 21 when given a input of 8. 

This approach is efficient due to the property of the Fibonacci sequence where each number is the sum of the two preceding ones. It limits the exponential growth of the recursive calls and makes the time complexity linear (O(n)). 

This function can be called with any positive integer n to retrieve the corresponding Fibonacci number. 
Let's make a slight improvement before closing this topic, let's optimize it further with a memoization technique to avoid redundant recursive calls. 

Here's the top-level code with comments to explain the logic effortlessly: 
```python
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    fib_value = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = fib_value
    return fib_value
```
In this optimized version, we introduce a memoization dictionary to store already calculated Fibonacci values to avoid redundant recursive calls. The function now uses the memoization dictionary to store and retrieve previously calculated Fibonacci values. It checks if the value for the current `n` exists in the memoization dictionary (`if n in memo`) before making any recursive calls. If the value is found, it returns the stored value directly, avoiding the unnecessary recursive calls.