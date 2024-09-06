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
This solution uses an iterative approach to calculate the Fib4 number sequence without using recursion. It uses 4 variables to store the values of the previous 4 steps and updates them iteratively in a loop. This allows the calculation of the n-th element efficiently and without recursion.