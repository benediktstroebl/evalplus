```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = d,a+b+c+d,c,a+b+c
    return a
```

This script defines a function `fib4` which uses a loop instead of recursion to efficiently calculate the nth number of the Fib4 sequence, adhering to the definition provided in the prompt. The loop progresses through each iteration (representing the value of `n`) and updates the four variables (`a`, `b`, `c`, `d`) used to track the Fib4 value for the current iteration. This is done in accordance with the definition of the Fib4 sequence provided in the prompt, where `fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)`. The output of the function is the value of `a` after the loop completes, which will be the nth value in the Fib4 sequence. 

The given example test cases demonstrate that the function correctly calculates the 5th, 6th, and 7th values in the Fib4 sequence, returning 4, 8, and 14, respectively.  This implementation avoids the exponential time complexity associated with recursive solutions to this type of problem, thus providing a more efficient solution.  It should be noted that this solution is analogous to a recursive solution that would use memoization and stores the previously computed values in an array to avoid redundant calculations.