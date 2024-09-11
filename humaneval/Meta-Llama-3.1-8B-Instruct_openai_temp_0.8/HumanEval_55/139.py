### Fibonacci Number Generator

Below is a Python script that implements a function to generate the nth Fibonacci number using both an iterative and a recursive approach.

```markdown
### Iterative Solution
```python
def fib_iterative(n: int) -> int:
    """
    Return n-th Fibonacci number using an iterative approach.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    
    fib_prev = 0
    fib_curr = 1
    
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next
    
    return fib_curr

### Recursive Solution
```python
def fib_recursive(n: int) -> int:
    """
    Return n-th Fibonacci number using a recursive approach.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    
    return fib_recursive(n - 1) + fib_recursive(n - 2)

### Test Cases
```python
print("Iterative Solution:")
print(fib_iterative(10))  # Output: 55
print(fib_iterative(1))   # Output: 1
print(fib_iterative(8))   # Output: 21

print("\nRecursive Solution:")
print(fib_recursive(10))  # Output: 55
print(fib_recursive(1))   # Output: 1
print(fib_recursive(8))   # Output: 21
```

**Optimizations:** 

- The iterative approach is generally more efficient than the recursive approach, especially for larger values of n, due to the overhead of function calls in the recursive approach. 
- The recursive approach also suffers from the issue of repeated calculations, where the same Fibonacci numbers are recalculated multiple times. This can be alleviated by storing the previously calculated values in a list or array and reusing them when needed.
- In the recursive approach, we can also use memoization to store the Fibonacci numbers and their indices, allowing us to retrieve the values directly instead of recalculating them. 
```python
def fib_recursive_memo(n: int, memo = {}) -> int:
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_recursive_memo(n - 1, memo) + fib_recursive_memo(n - 2, memo)
    
    return memo[n]
```

**Advice:**

- For larger values of n, the iterative approach with memoization is likely the most efficient and practical solution.
- For educational purposes or for small values of n, the recursive approach can be a useful way to understand the Fibonacci sequence and its properties.
- In real-world applications, consider using a caching mechanism to store previously calculated Fibonacci numbers and avoid recalculating them unnecessarily.