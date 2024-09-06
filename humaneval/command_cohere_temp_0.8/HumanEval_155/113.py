Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
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

This function takes an integer num as input and returns a tuple with two elements: one element is the count of even digits in num, and the other element is the count of odd digits in num. The overall time complexity of this code is O(W), where W is the number of characters in the string representation of the input number, which can be bounded by O(log(N)) where N is the number of digits in the number.

The code includes tests to verify the function's behavior:
```python
# Tests
assert even_odd_count.description == "Return number of even and odd digits in num."

assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(15) == (1, 1)
assert even_odd_count(898) == (2, 2)
``` 

These tests check the behavior of the even_odd_count function for different input numbers.