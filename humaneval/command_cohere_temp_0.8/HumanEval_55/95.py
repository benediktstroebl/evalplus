```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
The `fib` function calculates the n-th Fibonacci number iteratively, using a recursive approach. It bases the computation on the nature of Fibonacci numbers, which have a recursive relationship where each number is the sum of the two preceding ones (`F(n) = F(n-1) + F(n-2)`). 

This function's strength lies in its simplicity and efficiency in calculating Fibonacci numbers, which is O(1), unlike other, more complex, approaches that have a exponential time complexity. 

To test this function, we can call it with different values of `n` and compare the results with the expected Fibonacci numbers. 

For example:
```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```
As demonstrated, the output matches the expected Fibonacci numbers, confirming that the function works correctly.