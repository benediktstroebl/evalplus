```python
def skjkasdkd(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x**0.5) + 1, 2))]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out prime numbers from the given list of integers, then finds the largest prime number in that list, and finally converts it to a string summing its digits. The `all` function and the range with step 2 are used to perform the primality check via trial division with integers from 3 to the square root of the number.

To make the code more efficient and concise, it uses max(primes) to find the largest prime instead of using maximum loops, and map(int, ..) to transform the string of the sum of digits instead of using a list comprehension which would require additional transformations.

This solution has a time complexity of O(n\log(log(n))) for checking the primality of n, and O(n) for finding the maximum element in the list, resulting in an overall time complexity of O(n\log(log(n))). 

The space complexity is O(n) due to the creation of the primes list, but this can be mitigated by removing the requirement for the list comprehension to create a new list and instead iterate over the original list lst directly.  This would reduce the space complexity to O(1).