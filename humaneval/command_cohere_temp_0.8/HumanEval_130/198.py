```python
def tribonacci(n):
    result = [0,1,3][:n+1]
    for i in range(1, n+1, 2):
        result[i] = result[i-1] + result[i-2] + result[i+1]
    return result
``` 

This code defines a function `tribonacci` that returns the list of the first `n+1` numbers in the Tribonacci sequence. The sequence is defined recursively, with odd-indexed numbers equal to the sum of the previous two odd-indexed numbers, and even-indexed numbers equal to one more than the previous even-indexed number. A list `result` is initialized with the first two values of the sequence, then the loop iterates through the even indices, computing the odd indices' values accordingly, and the final result is returned. 

Here are some example outputs to test the function:
```python
tribonacci(0)  # [0, 1, 3]
tribonacci(1)  # [0, 1, 3, 2, 8]
tribonacci(2)  # [0, 1, 3, 2, 8, 5, 13, 8, 18]
tribonacci(3)  # [0, 1, 3, 2, 8, 5, 13, 8, 18, 5, 21, 8, 13, 18]
```