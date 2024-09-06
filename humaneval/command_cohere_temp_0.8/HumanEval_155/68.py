Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char <= '9' and char >= '0':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

And here is a test suite to ensure that the function correctly solves the problem:
```python
# Tests
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(15) == (1, 1)
assert even_odd_count(0) == (0, 0)
```