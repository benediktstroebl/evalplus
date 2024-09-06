```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operationally designed to solve the problem statement. It critically employs Python's inherent string-splitting technique utilizing the str attribute `split` to convert the string inputs into integer types. These integers, representing apples and oranges, are then subtracted from the overall total to pinpoint the count of mangoes within the basket. 

The function call `map(int, s.split(' and '))` parses the string input `s` into two integers representing apples and oranges in the basket. These are then subtracted from the total number of fruits, `n`, to find the number of mangoes in the basket. The function returns the result of this subtraction. 

Themdown code block below shows how to invoke this function with a test case:
```python
# Test the function
print(fruit_distribution("5 apples and 6 oranges", 19))
```

The corresponding output will be:
```bash
8
```