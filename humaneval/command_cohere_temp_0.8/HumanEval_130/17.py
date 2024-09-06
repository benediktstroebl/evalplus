```python
def tribonacci(n):
    result = [0,1,3]
    if n >= 1:
        result.extend( TribonacciHelper(n) )
    return result
        
def TribonacciHelper(n):
    # Handle edge case n=1
    if (n == 1):
        return [0]
    elif (n % 2 == 0):
        return [tribonacci(n-1) + tribonacci(n-2) + tribonacci(n) for i in range(n//2 + 1)]
    else:
        return [tribonacci(n-1) + tribonacci(n-2) + tribonacci(n+1) for i in range(n+1)]
```