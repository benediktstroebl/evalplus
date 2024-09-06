```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b,c+d,a+b+c+d
    return a

# Tests
assert fib4(0) == 0
assert fib4(1) == 0
assert fib4(2) == 2
assert fib4(3) == 0
assert fib4(4) == 3
assert fib4(5) == 4
assert fib4(6) == 8
assert fib4(7) == 14
```
This solution uses an iterative approach and stores the necessary values in variables to compute the n-th Fib4 number without recursion. 

Let's break down the solution step by step:
1. At the beginning of each iteration (for i in range(n):), the variables a, b, c, and d are updated to hold the values of the 4th, 3rd, 2nd, and 1st Fib4 numbers, respectively, for the current iteration.
2. The variables are updated in the order d, a, b, c, which is crucial to efficiently compute the current Fib4 number (a + b + c + d) for the current iteration.
3. At the end of each iteration, the variables are updated for the next iteration, which can be achieved since the Fib4 sequence is defined with the properties fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4). 

This solution does not use any additional memory beyond that required to store the handful of variables a, b, c, d. It is thus very memory-efficient, which is crucial for larger values of n. The solution also has a time complexity of O(n), which reflects the number of iterations needed to compute the n-th Fib4 number.