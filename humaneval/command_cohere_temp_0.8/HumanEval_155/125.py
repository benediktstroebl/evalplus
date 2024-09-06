Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return the number of even and odd digits in the integer."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1
    return even_count, odd_count
```

This function uses a couple of nested loops to iterate through each digit in the string representation of the input number, and counts the number of even and odd digits. Then, the function returns a tuple containing the counts.

To ensure that the function works correctly for all inputs, you might want to consider adding tests to the bottom of the script, evaluating different examples as demonstrated in the example you provided:
```python
# Tests
assert even_odd_count.description == "Return the number of even and odd digits in the integer.", even_odd_count.__doc__

assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(15) == (1, 1)
assert even_odd_count(enstein_cube(3)) == (3, 3)
``` 

This way, you can ensure your function works correctly for different input scenarios. 
If you want to learn more about testing, be sure to ask.