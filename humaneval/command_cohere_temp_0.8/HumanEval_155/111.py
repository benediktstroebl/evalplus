Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input num is expected to be an integer.")

    num_str = str(num)
    even_count = 0
    odd_count = 0

    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1

    return (even_count, odd_count)

# Example usage:
print(even_odd_count(-12))
print(even_odd_count(123))
```

This script will output the following:
```
(1, 1)
(1, 2)
```

The function begins by converting the integer num to a string, which allows us to iterate through its digits. We then maintain two counts: even_count and odd_count, which are incremented accordingly as we iterate through the digits of the number. Finally, the function returns a tuple containing these two counts. The code includes a validation check to ensure the input is an integer, and also provides example usage.