```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This approach uses a `count` array to keep track of the numbers that end with 1, iterating from 2 to `n` and accumulating counts in a `prefix sum` style, a number counting technique that starts with an initial value and then iteratively updates the counts by adding the values together, this allows to calculate the count of numbers that end with 1 without having to traverse the entire list each time. This works because the numbers that end with 1 are exactly the numbers from 2 to n inclusive, minus the numbers that start with 1. Therefore, the count of numbers that end with 1 is simply the count of numbers from 2 to n minus the count of numbers that start with 1, hence the subtraction of counts in the `counts` array.  This is a efficient solution using `O(n)` space and `O(n)` time.  It is also possible to solve this problem in `O(n)` time without using extra space, but that requires a different, more clever approach.  This approach is mentioned in the following paragraph.

An alternative approach that uses a more clever insight to solve this problem in `O(n)` time without using extra space is:
```python
def starts_one_ends(n):
    # Define a variable to store the answer
    count = 0
    
    # Loop through potential starting digits from 1 to n
    for digit in range(1, n + 1):
        # Determine if the current digit is a potential starting digit
        if digit == 1 or digit == n:
            count += 1
    
    # Return the calculated count
    return count
```

This solution hinges on the observation that the problem asks for the count of numbers that start or end with 1, and that the maximum possible number of digits (and hence the number of potential starting or ending digits) is `n`, the given upper bound of the positive integer's digits. This means that the numbers counting starts and ends both contribute to the total count, hence the double counting of the endpoints. This approach calculates this by iterating from 1 to `n` and adding `1` to the count for every digit that is equal to `1` or `n`, therefore efficiently solving the problem in `O(n)` time without extra space.  These are two alternative efficient solutions for the problem.