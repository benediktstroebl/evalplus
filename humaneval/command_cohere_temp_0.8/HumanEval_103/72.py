Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
The script defines a function `rounded_avg` that takes in two integers `n` and `m` as parameters. If `n` is greater than `m`, it returns -1. Otherwise, it calculates the average of integers between `n` and `m`, rounds the average to the nearest integer, and converts the result to binary.

The script returns the binary representation of the rounded average if the parameters are valid and return -1 if the smaller number is larger than the larger number. 

Let's break down the script further:
- The line `avg = (n + m) // 2` calculates the average of the two numbers.
- The condition `if n > m` checks if the starting number is greater than the ending number.
- The line `return -1` returns -1 as stated in the exercise if the starting number is greater than the ending number. 
- The line `return bin(round(avg))[2:]` converts the result to binary and returns the binary representation of the rounded average. 

This script provides a concise and efficient way to solve the problem as described. Let me know if you would like any clarifications or if there is anything else I can assist with! Hoped this was helpful! Let me know if you have any other questions.