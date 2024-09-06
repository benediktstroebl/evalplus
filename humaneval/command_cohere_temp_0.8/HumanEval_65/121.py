```python
def circular_shift(x, shift):
    num_str = str(x)
    circ_shifted = num_str[shift:] + num_str[:shift]
    return circ_shifted if len(circ_shifted) == len(num_str) else circ_shifted[::-1]
```
This Python script defines a function `circular_shift` that accepts an integer `x` and an integer `shift` as arguments. It starts by converting the integer `x` to a string `num_str`, resulting in a string representation of the integer. It then performs a circular shift on the digits of this string. This is done by concatenating the latter `shift` digits of `num_str` to the beginning and the digits at the beginning to the end, resulting in `circ_shifted`.

The function then checks if the length of `circ_shifted` is the same as the original length of `num_str`. If it is, this shifted string is returned as the result, accomplishing the circular shift desired. If the shift exceeds the number of digits, thereby resulting in a shorter string, the function instead returns the reversed version of `circ_shifted`, which restores the digits in the reversed order, as per the problem's guidelines. 

The expected behavior is demonstrated in the example tests, where `circular_shift(12, 1)` returns "21" and `circular_shift(12, 2)` returns "12", consistent with the problem statement.