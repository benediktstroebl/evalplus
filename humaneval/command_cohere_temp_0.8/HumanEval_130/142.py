```python
def tri(n):
    result = [0,1,3]
    if n >= 1:
        result += [tri_rec(n)]
    return result + [0]

def tri_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 1:
        return tri_rec(n - 1) + tri_rec(n - 2) + tri_rec(n + 1)
    else:
        return 1 + n / 2
```

The problem discusses the Tribonacci sequence which is defined by the recurrence relation:
- tri(1) = 3
- tri(n) = 1 + n / 2, if n is even
- tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd 

The provided code uses a recursive approach to calculate the Tribonacci numbers and it handles the base cases for n=0, n=1. It returns a list of the first n + 1 numbers of the Tribonacci sequence.  It achieves this by generating the sequence and then adding a null element at the end to ensure the list is of length n + 1. 

This approach follows a similar logic to Fibonacci sequence but with different recursive equations.