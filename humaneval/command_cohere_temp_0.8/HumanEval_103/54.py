Here's a Python script that includes a function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The script provides a function that:
- Calculates the average of numbers from `n` to `m` (including both).
- Checks whether `n` is greater than `m`, and if so, returns `-1`.
- Rounds the average to the nearest integer.
- Converts the rounded value to binary and returns the result.

The function is self-contained and can be used as a standalone function in other Python scripts. 

Let's break down the solution into components for clarity:
1. Calculating the Average:
   ```python
   avg = (n + m) // 2
   ```
   The average is computed using the well-known formula for the average of the first `x` and `y` numbers, `(x + y) / 2`.

2. Handling Boundary Conditions:
   ```python
   if n > m:
       return -1
   ```
   This condition handles the case where `n` is greater than `m`. The function ensures that this situation is handled correctly by returning `-1`.

3. Rounding and Binary Conversion:
   ```python
   return bin(round(avg))[2:]
   ```
   The average value is rounded to the nearest integer using the `round()` function. Subsequently, the result is converted to binary using the `bin()` function. Note that we retrieve the binary representation from the returned string with `bin(round(avg))[2:]`, as the `bin()` function returns a string representing the binary value with a leading `'0b'` prefix.

The solution adheres to the problem statement and provides the expected binary representation of the rounded average. You can use this function independently to tackle scenarios as per the problem statement.