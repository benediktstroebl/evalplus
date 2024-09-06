```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i  # return the larger of i or j
    return 1  # if no factors, return 1
```

The function largest_divisor takes an integer n as input and searches for factors of n. It iterates through numbers from 1 to n-1, checking if the current number divides n with no remainder. If it does, the function calculates the divisor as n/current_number. It then returns the largest divisor smaller than n, which is the purpose of the mission. If no factors are found, the function returns 1. This approach ensures finding the largest divisor within the given constraints.