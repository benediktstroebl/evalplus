```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It bases the computation on the fact that the n-th Fibonacci number may be expressed as the sum of the (n-1)-th and (n-2)-th Fibonacci numbers. As a result, the function recursively calls itself with the arguments (n-1) and (n-2), then adds the results to provide the solution. This strategy efficiently uses mathematical linkages to reach the required answer.

Here is an example of using the function with a specific value of `n` and showing the corresponding output:
```python
n = 10
result = fib(n)
print(f"The {n}-th Fibonacci number is: {result}")
```

This would produce the following result:
```
The 10-th Fibonacci number is: 55
```

This demonstrates the function's ability to calculate the 10th Fibonacci number, emphasizing its correctness and efficiency in handling Fibonacci sequences.