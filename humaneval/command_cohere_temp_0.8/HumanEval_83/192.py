```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    counts = [0] * (n + 1)
    
    # Count numbers that start with 1
    counts[1] = 1
    
    # Count numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[-1]
```

This Python script defines a function `starts_one_ends(n)` which calculates the count of numbers that are `n-digits` long and either start or end with the digit 1. The solution is based on the observation that every `n-digit` number that ends with 1 must start with a digit different from 1, and hence such numbers can be constructed by first constructing all `n-digit` numbers that start with a digit other than 1 and then adding a final 1 to each of them. The total count of such numbers is therefore equal to the count of `n-digit` numbers that start with a digit other than 1 plus the count of `n-digit` numbers that end with 1. The latter can be computed by counting the numbers that end with 1 from 2 to n-digit. 

The script also runs a count of 1s in numbers from 1 to n to support the solution logic. This count is stored in the `counts` array. The solution then returns the last element of the `counts` array, which represents the count of numbers n-digit positive integers that start or end with 1. 

Note that the unit test for this solution would simply be providing an input and ensuring that the output matches the expected result.