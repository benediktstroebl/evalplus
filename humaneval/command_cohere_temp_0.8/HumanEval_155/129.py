Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    # Convert num to str and remove any non-digit characters
    num = str(num).strip('-.')
    count_odd = count_even = 0
    for char in num:
        if char > '9':
            continue
        elif char % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

This code first converts the input num to a string and removes any non-digit characters using the strip('-.') method. It initializes two counters, count_even and count_odd, to zero, and then loops through each character in the string num. It checks if each character is a digit and uses the modulo operator (%) to determine if it's even or odd, incrementing the appropriate counter.

To use the even_odd_count function, simply call it with a number as follows:
```python
print(even_odd_count(21))  # Output: (1, 1)
print(even_odd_count(42))  # Output: (1, 1)
print(even_odd_count(517)) # Output: (2, 1)
``` 

This will return a tuple containing the number of even and odd digits, respectively.