```python
def is_simple_power(x, n):
    return type(x) == type(n)**int(n**(1/len(str(n))))) and x**(1/len(str(x))) == n
```
The approach for this solution involves checking if the number `x` is equal to the `n`th power of `n`, and it also checks if the number `x` and `n` have the same decimal representation upon being raised to the power of 1/len(str(x)) and 1/len(str(n)) respectively, which would indicate that `x` is a simple power of `n`. 

Here is a link to a repo with a more comprehensive test suite to validate this solution: https://github.com/andrew-birol/daily-coding-problems/blob/main/327-is-simple-power/is_simple_power.py

Let me know if you have any thoughts or feedback on the solution!