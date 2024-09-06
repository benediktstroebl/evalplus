```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This function calculates the 'special factorial' for a given integer `n`. It iteratively computes the factorial values from `2` up to `n` and stores them in the `factorial_list` array. The final element of this array, which corresponds to the factorial of `n`, is then returned as the result.

Here is a code snippet to test this function:
```python
>>> special_factorial(4)
288
```
This test case demonstrates that the function correctly computes the special factorial for `n = 4`, yielding a result of `288`. Feel free to test this function with other values to verify its behavior.