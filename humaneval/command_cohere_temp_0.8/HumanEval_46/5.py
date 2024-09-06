```python
def fib4(n):
    prev = [0, 0, 2, 0]
    for _ in range(4, n + 1):
        curr = prev[-1] + prev[-2] + prev[-3] + prev[-4]
        prev.append(curr)
    return prev[-1]
```
This script defines a function `fib4` that uses an iterative approach to calculate the nth number of the Fib4 sequence, supporting test cases provided in the prompt. 
The overall time complexity of the function is O(n) due to the loop iterating n times, and the constant factors involved in arithmetic operations and list operations are negligible. Thus, this function efficiently computes the nth element of the Fib4 sequence in linear time.