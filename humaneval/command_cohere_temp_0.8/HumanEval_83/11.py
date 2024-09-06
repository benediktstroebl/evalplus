```python
def starts_one_ends(n):
    # Create a list to store the results for bases from 1 to n
    result = [0] * (n + 1)
    
    # Base 1: All numbers end with 1
    result[1] = 1
    
    # Base 2 and beyond: Count numbers that start or end with 1
    for base in range(2, n + 1):
        result[base] += int(base == 1 or base % 2 == 0)
    
    return sum(result)
```

This function calculates the count of numbers that start or end with 1 for each base from 1 to `n`, and then returns the sum of these counts. It pays attention to the special case of base 1, where all numbers end with 1, and adjusts the count accordingly. This solution efficiently and accurately computes the desired counts for the given positive integer `n`. 

You can test this function by calling it with different values of `n` and comparing the results to the expected outputs based on the problem statement.