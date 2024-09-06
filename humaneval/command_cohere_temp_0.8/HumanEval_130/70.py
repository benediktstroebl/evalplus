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
The function `tribonacci` implements the Tribonacci sequence, it uses base cases for n=0, n=1, and then employs an if-else structure to calculate the Tribonacci numbers for any `n` using the definition of the Tribonacci sequence. This approach effectively calculates the required list of Tribonacci numbers for any positive integer `n`.  It is important to note that since the sequence is infinite, the function returns a list of numbers up to the `n`-th term of the sequence.