Here's a Python script that contains a function called even_odd_count, defined to take in an integer num and return a tuple containing the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    num_str = str(num)
    count_even = 0
    count_odd = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    return (count_even, count_odd)
```

And here is a test suite to ensure that the function behaves as expected:
```python
# Tests:
assert even_odd_count. explan == "Given an integer. return a tuple that has the number of even and odd digits respectively."
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(15) == (1, 1)
assert even_odd_count(14) == (0, 1)
assert even_odd_count(17200000000000) == (5, 7)
```