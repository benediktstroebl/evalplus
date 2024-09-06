Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    binary_str = '-1' if n > m else bin(round((n + m) / 2)).split('b')[1]
    return binary_str if n != m else binary_str[0]
```
This script provides a function that solves the problem as outlined in the example test cases provided. 

It rounds the average to the nearest integer and returns -1 if n is greater than m. The bin() function converts the integer to a binary string, and the expression bin(round((n + m) / 2)).split('b')[1] ensures that only the binary string without the 'b' prefix is returned. If n and m are the same, it returns just the first binary digit due to the string indexing syntax binary_str[0].