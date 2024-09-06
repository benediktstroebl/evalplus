```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for digit in digits if digit % 2 == 1)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

The code uses a generator expression and the `sum` function to count the odd digits in each string and places it in a list. The result is then formatted as required by the problem statement. This solution is efficient because the code runs in linear time, O(n), where n is the length of the list of strings. Also, the space complexity is O(n) due to the creation of a new list to store the results. 

This solution is somewhat simplistic as it does not employ any explicit iteration through the strings and instead leverages list comprehension and the `sum` function. 

This solution assumes that the input list contains strings consisting only of digits, as per the problem statement. If the input list is not adequately sanitized, unexpected errors may occur. It is vital to ensure that the input is correctly validated and sanitized before executing the function.