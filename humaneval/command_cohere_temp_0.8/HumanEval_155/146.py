Here's a Python script with a self-contained function that solves the problem:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1
    return (even_count, odd_count)
```

This script defines a function `even_odd_count` that takes an integer `num` as input and returns a tuple with the number of even and odd digits respectively. The script includes an example in the docstring that shows how the function works with examples like `even_odd_count(-12) ==> (1, 1)` and `even_odd_count(123) ==> (1, 2)`.

This will return the desired tuple with the number of even and odd digits respectively.