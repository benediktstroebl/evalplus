```python
def choose_num(x, y):
    max_even = max(x, y)
    floor_even = max_even - 1
    if floor_even % 2 == 0:
        return floor_even
    else:
        return -1
```

The function 'choose_num()' takes two positive numbers 'x' and 'y' and returns the biggest even integer that falls in the range '[x, y]'. If the range does not contain an even integer greater than or equal to 'x', the function returns -1. 

Here's an example of how you can test this script:
```python
# Test Case 1
x = 12
y = 15
result = choose_num(x, y)
assert result == 14

# Test Case 2
x = 13
y = 12
result = choose_num(x, y)
assert result == -1
```

This will verify that the 'choose_num()' function performs as expected.