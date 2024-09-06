```python
def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Handle the case where n = 1
    if n == 1:
        return 2
    
    # Handle the case where n is even (the number starts with 1 and ends with 1)
    if n % 2 == 0:
        return digits[0]
    
    # Subtract cases where the number ends with 1 (not considering the starting 1)
    return digits[0] - digits[n // 2] + 1
```

This script assumes that the input `n` is a positive integer greater than 1, leading with and ending with '1'.

For better style and readability, the function directly assigns the result for n = 1 and n = 2. From n = 3 onwards, it uses a more efficient approach. It creates a list of digits from 1 to n and then subtracts the count of ending 1s (excluding the starting 1). Finally, it adds 1 to account for the starting 1. This strategy avoids repeatedly subtracting and adding 1. 

 hashtable: Here be magic!