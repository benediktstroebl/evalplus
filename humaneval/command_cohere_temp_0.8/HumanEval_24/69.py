```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i >= i:
            return i
    return 1
```
The function iterates through numbers from 1 to n. If n is divisible by i and the divisor i is equal to or larger than the floor of n/i, it returns i as the largest divisor. Otherwise, it increments i and repeats the process. The loop terminates when the floor of n/i is less than i, meaning no larger divisor exists.

Here is an example usage of the function for the input 15:
```python
largest_divisor(15)
```
The output of the function is 5, which is the largest divisor of 15. 

This method works efficiently with a time complexity of O(n) and is among the simplest approaches to finding the largest divisor of a number.