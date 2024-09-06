```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tribonacci(n - 1)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```
The function takes an input of type integer and returns a list of numbers for the Tribonacci sequence, based on the definition of the Tribonacci sequence as described in the problem statement. The function recursively divides the problem into 3 categories:
1. `n == 0`: In this case it returns [0] regardless of the `n`
2. `n == 1`: In this case it returns [1] regardless of the `n`
3. `n % 2 == 0`: This is for the even numbers, in which we have a recurrence relation of `tri(n) = 1 + n / 2` 

Therefore, the returned list is formed by concatenating an extra 0 at the beginning (to denote the zero value for even indices, according to the problem's definition), followed by a recursive call to tribonacci(n-1).

Elsewise, it returns a list that starts with the number 1 (denoting the one value for odd indices, according to the problem's definition), followed by a recursive call to tribonacci(n-1) concatenated with a call to tribonacci(n-2) and tribonacci(n+1). This is based on the recurrence relation for the odd indices: `tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1)`.