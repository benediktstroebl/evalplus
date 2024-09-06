Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char != ' ':
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

This function evaluates the given integer and returns the number of even and odd digits in the integer as a tuple, handling whitespace as a neutral element. 

You can test this function by calling it with different integers to verify the results:
```python
# Test cases
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(10) == (2, 0)
assert even_odd_count(21) == (2, 1)
```

Note that the implementation assumes that integers are passed into the function, and that the behavior can be undefined for non-integer inputs.