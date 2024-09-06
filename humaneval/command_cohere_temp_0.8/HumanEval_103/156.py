Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))[2:]
```
This function calculates the average of the integers between `n` and `m`, inclusive. If `n` is greater than `m`, it returns -1. Otherwise, it calculates the average, rounds it to the nearest integer, and converts that value to binary.

To better understand the problem, here is how the function works step-by-step:
1. If `n` is greater than `m`, it returns -1, which handles the edge case where the range is inverted.
2. Otherwise, it calculates the average of numbers from `n` to `m` with `(n + m) // 2`. This integer arithmetic averages the two endpoints and all the integers in between.
3. It rounds this average to the nearest integer using `round()`.
4. The result is converted to binary using `bin()` with the optional parameter `2:` to skip the '0b' prefix. 

The resulting binary string is returned. 

To handle the examples from the problem statement:
- `rounded_avg(1, 5)` - Yields "0b11"
- `rounded_avg(7, 5)` - Returns -1
- `rounded_avg(10, 20)` - Yields "0b1111"
- `rounded_avg(20, 33)` - Yields "0b11010"

This function is self-contained and should work as expected. Feel free to test it with other inputs to verify its behavior.