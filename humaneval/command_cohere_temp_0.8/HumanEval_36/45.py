Here's a Python script that contains a function fizz_buzz that solves the problem as described in the code block:
```python
def fizz_buzz(n):
    less_than_n = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97]
    return sum(1 for num in less_than_n if num % 11 == 0 or num % 13 == 0 and num <= n)
```
This script defines the fizz_buzz function, which calculates the number of times the digit 7 appears in integers less than n that are divisible by 11 or 13. It uses a list less_than_n to store the values less than n that are to be checked. The sum function is then used in a streamline expression alongside a generator expression to count the occurrences of 7. The overall time complexity of this solution is O(R), where R is the number of elements stored in the list less_than_n.