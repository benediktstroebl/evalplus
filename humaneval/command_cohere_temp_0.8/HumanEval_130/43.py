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

The function takes an input of type integer `n` and returns a list of the first `n + 1` numbers of the Tribonacci sequence following the definition provided in the problem statement. The base cases are defined as:
- `tribonacci(0) = [0]`
- `tribonacci(1) = [1]`

For any other `n`, the Tribonacci number at that index is determined by the following rules:
- If n is even, it's the sum of the two Tribonacci numbers previous to it.
- If n is odd, it's the sum of the previous, current, and next Tribonacci numbers.

This recursive approach mirrors the definition provided in the problem statement, creating a list of Tribonacci numbers from the provided initial values, where the base cases handle the first two indices. It is important to note that this solution has an exponential time complexity and is not the most efficient approach. For larger values of n, this approach will result in a stack overflow error. There are other solutions that use a more iterative approach. 

You can test this function by calling `tribonacci(n)` where n is the index of the Tribonacci number you want to retrieve from the sequence.