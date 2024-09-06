Here is a Python script that solves the given problem:
```python
def f(n):
    li = []
    for i in range(1, n+1):
        if i % 2 == 0:
            li.append(factorial(i))
        else:
            li.append(sum(range(1, i+1)))
    return li

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```
The function `f` takes an integer `n` as input and creates a list where the element at index `i` is the factorial of `i` if `i` is even, or the sum of numbers from `1` to `i` otherwise. The `factorial` function is also provided to calculate the factorial of a given number using a loop. This code will work correctly for the given example and any other input that satisfies the problem statement. 
The code includes the `example` clause, which is not part of the function definition nor any assigned variable. To remain compatible with the problem statement, I added the example test case to the code as follows:
```python
print(f(5))  # [1, 2, 6, 24, 15]
```

This way, the code is self-contained and can be verified against the described functionality.  If you only want the function `f` without the example, let me know, and I'll revise it for you.