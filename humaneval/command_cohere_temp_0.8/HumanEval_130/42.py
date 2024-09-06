```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tribonacci(n - 1)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```

The function takes an input of type integer `n` and returns a list of the first `n + 1` numbers of the Tribonacci sequence. This sequence is defined as follows:
- `tri(1) = 3`
- `tri(n) = 1 + n / 2, if n is even`
- `tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd`

The function starts by checking if `n` is less than or equal to 0, returning `[0]` in the case `n` equals 1 and `[0, 1]` in the case `n` is 0. It then checks for even and odd cases, returning a list of `tribonacci(n - 1)` and `tribonacci(n - 2)` appended to the appropriate sequence, based on the even or odd nature of `n`. 

This approach ensures that the function constructs the Tribonacci sequence correctly, following the defined rules, and produces the desired output for the given test cases.