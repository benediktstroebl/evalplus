```python
def count_sevens_divisible(n: int):
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive) for counting.
    
    Returns:
    int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    
    # Initialize a counter for the digit 7
    count = 0
    
    # Iterate over all numbers less than n
    for i in range(1, n):
        
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            
            # Convert the number to a string to easily count the digit 7
            str_i = str(i)
            
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    
    # Return the total count of the digit 7
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens_divisible(n)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```
This script defines two functions: `count_sevens_divisible` counts the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13, and `fizz_buzz` calls `count_sevens_divisible`. The script includes test cases to verify that the functions work as expected.