```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    else:
        return [1, 3, 2] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an input of type integer and returns a list of the first n + 1 numbers of the Tribonacci sequence following the specification that you provided in the problem. Note that the function also handles the edge cases n = 1 and n = 0, which are necessary to provide a full solution to the problem. 

To make this solution more efficient and reduce the number of recursive calls, we can use the explicit iteration method, similar to the Fibonacci sequence using memoization. Below is a more optimized version of the code:
```python
def tribonacci(n, memo={}):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    if n not in memo:
        memo[n] = [1, 3, 2] + tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n + 1, memo)
    return memo[n]
```
This version uses a dictionary called `memo` to store the already calculated values of the Tribonacci sequence, avoiding the need for redundant calculations when multiple values are requested in a single call. 

To handle larger inputs without spending too much time on calculation, you can use iterative methods to calculate tribonacci(n) in O(n) time, which is much better than the recursive approach's O(n^2) runtime.