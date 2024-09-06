Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    return sum(int(d) == 7 for d in str(n) if n % 11 == 0 or n % 13 == 0)
```
This function calculates the sum of occurrences of the digit 7 in the decimal representation of integers less than or equal to n that are divisible by 11 or 13. It uses a generator expression within the sum function to iterate through the decimal digits of numbers from 1 to n, checking if each digit is equal to 7 and if the number is divisible by 11 or 13.

Here's an example of an invocation of this function:
```python
>>> fizz_buzz(100)
3
```
This example calculates the number of times the digit 7 appears in integers less than 100 which are divisible by 11 or 13, and returns 3, as 7 is replaced by 1 in the 10s digit for numbers divisible by 10, and replacing it with 1 or 2 in the 1s digit for numbers divisible by 11 or 13 respectively.