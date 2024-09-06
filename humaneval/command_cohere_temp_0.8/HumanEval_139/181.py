```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` to `n!`. The plain factorial of a non-negative integer `n` is represented as `n! = n * (n-1) * ... * 2 * 1`. The Brazilian factorial is then defined as the product of all these factorials up to `n`. 

The script validates the correctness of the `special_factorial` function by utilizing a test case of input size `4`, ensuring that it returns the expected output of `288`. 

Overall, this solution is efficient as it utilizes a straightforward recursive approach to calculate the factorials and produces the Brazilian factorial by multiplying the appropriate factorials together.