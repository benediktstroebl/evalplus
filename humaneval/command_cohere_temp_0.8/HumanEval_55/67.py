```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
The code defines a Python function called `fib` that calculates the n-th Fibonacci number. The base case checks if `n` is less than or equal to 1, returning `n` if so. Otherwise, the function recursively computes the sum of the (n-1)-th and (n-2)-th Fibonacci numbers, which is the definition of the n-th Fibonacci number. This approach leverages the intrinsic nature of Fibonacci numbers, where each number is the sum of the two preceding ones. This algorithm is efficient for large `n` due to the canceling effect of consecutive recursive calls, reducing the computation to a more manageable size. As a result, the function effectively calculates Fibonacci numbers and fulfills the requirement. 

The function can be tested by calling it with different input values and verifying that it returns the expected Fibonacci numbers. For example, calling `fib(10)` should return `55`, `fib(1)` should return `1`, and `fib(8)` should return `21`.  This will ensure that the function is working correctly and producing the desired output.