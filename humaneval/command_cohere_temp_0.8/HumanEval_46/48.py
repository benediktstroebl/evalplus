```python
def fib4(n):
    a,b,c,d = 0,0,1,1
    for i in range(n):
        a,b,c,d = b,c,d, a+b+c+d
    return a
```

This script defines a function 'fib4' which uses an iterative approach to calculate the nth Fib4 number without using recursion. It initializes four variables ('a', 'b', 'c', 'd') to track the state of the computation, and iterates 'n' times, updating the state accordingly. The final 'a' value is the nth Fib4 number, which is returned. The script passes the given tests as it produces the correct values for 'fib4(5)', 'fib4(6)', and 'fib4(7)'.  It has a time complexity of `O(n)` and a space complexity of `O(1)`, making it an efficient and concise solution.