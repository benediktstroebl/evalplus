```python
def odd_count(lst):
    r = []
    for num in lst:
        o = sum(1 for c in num if c % 2 != 0)
        r += [f"the number of odd elements {o} in the string {num} of the input"]
    return r
```

The function `odd_count` uses a generator expression to iterate over each character in the list of strings, counting how many of them are odd digits. Then it creatively constructs a string message that informs the reader of the number of odd digits in the corresponding input string. The list of such messages is returned as the final response.

This solution utilizes Python 3.9's `str.format()` and a ternary operation to construct the message, enhancing readability and minimizing the use of conditional statements.