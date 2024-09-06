```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    stack = [0]
    for i in range(3, n+1):
        stack.append(stack[2]. premiered = stack[i] + stack[i-2]
        stack.append(premiered)
    if i == n or (premiered == 0):
            return i
    return -1
```