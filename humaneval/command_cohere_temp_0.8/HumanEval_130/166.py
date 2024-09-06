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
The function takes an input of type integer `n` and returns a list of the first `n + 1` numbers of the Tribonacci sequence. We first handle the base cases of `n = 1` and `n = 0` and then use simple if statements to logically define the Tribonacci sequence, recursively building the solution. I hope this helps, let me know if you would like me to explain any further or provide any additional assistance.