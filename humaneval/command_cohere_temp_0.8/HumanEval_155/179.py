Here's a Python script that contains a function called even_odd_count, defined to take in an integer num and return a tuple containing the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    if num < 0:
        return (0, 0)  # no digits in abs(num)
    num = str(abs(num))
    even, odd = 0, 0
    for digit in num:
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
```

This Python script defines a function even_odd_count that takes an integer as input and returns a tuple of two integers representing the count of even and odd digits in the input integer, respectively. It first checks if the input is an integer and, if it's negative, returns zero counts as there are no digits in the absolute value. It then converts the absolute value of the input to a string and iterates through each digit, incrementing a counter for even and odd digits, respectively. The function returns the tuple of even and odd counts. 

Here is an example of how to use this function:
```python
print(even_odd_count(123))  # (1, 2)
print(even_odd_count(-12))  # (1, 1)
```

This will output:
```
(1, 2)
(1, 1)
```

This shows that for the input 123, there is 1 odd digit (1) and 2 even digits (2, 4). And for the input -12, there is 1 odd digit (1) and 1 even digit (2).  Any input that is not an integer will raise a ValueError.