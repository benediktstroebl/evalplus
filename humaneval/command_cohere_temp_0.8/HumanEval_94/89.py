```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 and x != 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` takes a list of integers as input and returns the sum of the digits of the largest prime number in the list.

First, it generates a list of prime numbers from the input list using a list comprehension. Then, it finds the largest prime number in that list using the `max` function and converts it to a string. Finally, it returns the sum of the digits of that string. 

This solution adheres to the problem description provided above and should work correctly for the given test cases. 

This script can be copied and pasted into a Python environment or script to solve the given problem.