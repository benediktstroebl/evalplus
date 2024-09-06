```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Anchor the loop to hunt for the largest divisor
            if j > i:  # Update i if j is larger to hunt for a larger divisor
                i = j
            if i > largest_divisor.result:
                largest_divisor.result = i  # Keep track of the largest divisor encountered
    return largest_divisor.result
```
The function largest_divisor keeps track of the largest divisor encountered while iterating through all factors of n using the largest_divisor.result variable. This ensures a linear time complexity of O(n) to find the largest divisor. The idea is to anchor the loop to hunt for the largest divisor by dividing n by i and storing the anchor in j. Thus, the largest divisor is the largest factor of n that is less than n, which is the objective of the given problem.  This approach solves the problem in a single loop, making the solution efficient and straightforward.