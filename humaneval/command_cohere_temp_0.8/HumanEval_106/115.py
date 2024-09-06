Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    ls = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ls.append(factorial(i))
        else:
            ls.append(sum(range(1, i+1)))
    return ls

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Tests:
print(f(5))
# [1, 2, 6, 24, 15]
```
The function `f` takes an integer `n` as input and creates a list where the value of the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from 1 to `i` otherwise. The function uses the recursive `factorial` function to calculate the factorial of even indices. Would you like to know more about the code?