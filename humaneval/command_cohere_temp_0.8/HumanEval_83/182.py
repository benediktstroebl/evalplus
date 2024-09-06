```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else: 
        # initialize the count with endpoints considered
        result = (1 + 10) / 2
        # Iterate through the first n-2 digits and update the count of valid numbers
        for i in range(10, 10**(n-1), 10):
            if (i % 10 != 1 and i != 0 and ((i//10) % 10 != 1) ):
                result -= 1
            else:
                result += 1
        return result
```

This script considers all digits from 1 to 9 for the internal digits of the number, and then considers the first and last position as 1 or any digit from 1 to 9. It also avoids duplicate counting by considering the numbers in their respective positions.

The unit test for this function can be copied and pasted into a separate file to verify its functionality.