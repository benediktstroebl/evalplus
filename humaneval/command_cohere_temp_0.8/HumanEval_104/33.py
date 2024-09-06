Here's a Python script that contains a function called unique_digits, which solves the problem you've described:
```python
def unique_digits(ls):
    even_digits = [ele for ele in ls if any(int(digit) % 2 == 0 for digit in str(ele))]
    return sorted(ele for ele in ls if not ele in even_digits)
```

This function takes a list of positive integers as input and returns a sorted list of all elements that do not have any even digits. The function uses a list comprehension to generate a list of all elements that have at least one even digit, then returns a sorted list of all elements not contained in this list. Finally, the function solves the given problem statement and returns the expected result.