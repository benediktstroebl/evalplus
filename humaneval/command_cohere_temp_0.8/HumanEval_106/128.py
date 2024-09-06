Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def f(n):
    ans = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ans.append(factorial(i))
        else:
            ans.append(sum(range(1, i+1)))
    return ans

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
```
The `f` function uses two loops: one to iterate through the indices from 1 to `n`, and another within a `conditional test` to determine whether the index `i` is even or odd. If the index `i` is even, the `factorial` function is called to calculate the factorial of index `i`, which is then appended to the `ans` list. If the index `i` is odd, the sum of numbers from 1 to `i` is calculated and appended to the `ans` list. The `factorial` function, on the other hand, uses an iterative approach to calculate the factorial of a given number `n` by multiplying the `num` variable by all numbers from 1 to `n`. 
This solution is efficient given the problem constraints.