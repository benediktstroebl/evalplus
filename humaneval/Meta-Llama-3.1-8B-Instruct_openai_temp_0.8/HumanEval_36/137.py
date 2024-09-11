```python
def count_sevens(n: int):
    """
    Count the number of times the digit 7 appears in integers less than n.
    
    Args:
    n (int): The upper bound (exclusive) for counting digit 7.
    
    Returns:
    int: The count of digit 7.
    """
    count = 0
    for i in range(1, n):
        # Convert the number to a string to easily iterate over its digits
        for digit in str(i):
            # Check if the digit is '7'
            if digit == '7':
                # Increment the count
                count += 1
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper bound (exclusive) for counting digit 7 in multiples of 11 or 13.
    
    Returns:
    int: The count of digit 7 in multiples of 11 or 13.
    """
    # Count digit 7 in all numbers less than n
    total_count = count_sevens(n)
    
    # Count digit 7 in multiples of 11 and multiples of 13
    count_11 = count_sevens(n // 11)
    count_13 = count_sevens(n // 13)
    
    # Subtract the counts of digit 7 in numbers that are multiples of both 11 and 13
    count_11_13 = count_sevens(n // (11 * 13))
    
    # Apply the inclusion-exclusion principle to get the correct count
    return total_count - count_11 - count_13 + count_11_13


# Test the function
if __name__ == '__main__':
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```

This script first defines a helper function `count_sevens` that counts the number of times the digit 7 appears in integers less than a given number. The `fizz_buzz` function uses this helper function to count the number of times the digit 7 appears in integers less than a given number that are divisible by 11 or 13, applying the inclusion-exclusion principle to avoid double counting multiples of both 11 and 13.