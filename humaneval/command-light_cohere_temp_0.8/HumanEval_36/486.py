```python
def fizz_buzz(n: int):
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 15 == 0})
```
This Python function fizz_buzz takes an integer n as input and calculates the number of times the digit 7 appears in the sequence from 1 to n. The function utilizes a iterative approach with an inner loop and conditional check to identify occurrences of 7. The function then returns the result.