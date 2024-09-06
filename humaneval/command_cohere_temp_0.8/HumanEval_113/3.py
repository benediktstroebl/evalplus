```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for digit in digits if digit % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

This solution leverages Python's str.format() method to construct the output string with the count of odd digits. The sum() function is used to count the number of odd digits in each string, and the result is converted to a string using str(). The string formatting then replaces the placeholder '{}' with the count of odd digits in each string. 

Such problems are good opportunities to use string formatting and Python's ability to construct complex strings from expressions. These features are part of Python's powerful string manipulation capabilities. 

This solution is concise and achieves the required output format, making it an optimal solution for the problem at hand.