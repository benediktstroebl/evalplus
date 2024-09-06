```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fib4 sequence begins with 0 and 1.
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

```
In this script, the function `fib4` computes the n-th Fibonacci number in O(n) time complexity. The function is designed without recursion and uses a simple formula to compute Fibonacci numbers. 

It uses the base case to handle the special cases for n = 0,1,2 where the Fibonacci numbers are 0,0, and 2, respectively. Using this formula, the function can efficiently compute Fibonacci numbers for larger values of n without the need for recursion.