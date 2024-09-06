```python
def starts_one_ends(n):
    return (10 ** (n-1)) + 9 * (10 ** (n-1) - 1)
```

This function calculates the count of numbers that start or end with 1 for n-digit positive integers using the formula `(10 ** (n-1)) + 9 * (10 ** (n-1) - 1)`. This takes into account the cases where the first digit is 1 and the cases where the last digit is 1, effectively doubling the count.

The argument `n` represents the length of the positive integer, which will be greater than or equal to 1. This function directly returns the count of valid numbers and does not require any explicit loops or arrays to iterate over numbers, making it efficient for larger values of `n`. 

This solution is elegantly simple and directly applies the provided formula to calculate the total count of numbers that start or end with 1, making it both effective and efficient. 

If you would like to efficiently iterate through further permutations and possibilities, we can optimize the approach further. Feel free to provide the specific details of the next problem, and I'll be glad to tailor a solution to it.