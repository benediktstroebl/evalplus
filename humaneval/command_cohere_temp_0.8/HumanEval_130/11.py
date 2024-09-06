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
The function takes an input integer `n` and returns a list of the first `n + 1` numbers in the Tribonacci sequence, which is defined by the recurrence relation mentioned in the problem statement. This list is then passed to the `print` function to output the Tribonacci sequence for the given value of `n`. The markdown code block can be added to a `.md` file or directly in your collaboration drive or text document and execute the Python script independently to see the output.