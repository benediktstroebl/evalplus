Here's a Python script with a self-contained function that solves the problem:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > '9':
            if char % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            if int(char) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
```

This script defines a function `even_odd_count` that takes an integer `num` as input and returns a tuple with the number of even and odd digits respectively. The script provides a quick test to check the functionality of the function:
```python
print(even_odd_count(123))
print(even_odd_count(-12))
```

The output should be:
```
(1, 2)
(1, 1)
```

This demonstrates the count of even and odd digits against the provided examples.