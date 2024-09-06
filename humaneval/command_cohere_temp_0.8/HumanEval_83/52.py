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

This approach uses a clue from the word problem: **the numbers have to be positive**. The code initializes a list `counts` where each element `counts[i]` represents the count of `i-digit` positive numbers that start or end with 1. It then iterates through the digits from 2 to `n`, incrementing the count of numbers that end with 1, and finally, this count is retrieved from the `counts` array. 

The solution works because if digits[k] forms the last digit of the number, then the number ends with 1. And if digits[k] is not the last digit of the number, then the number starts with 1. Thus, the count of numbers that end with 1 is just the count of numbers that start with 1, shifted by one.