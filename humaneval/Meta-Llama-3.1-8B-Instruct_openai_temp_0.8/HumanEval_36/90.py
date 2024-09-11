```python
def count_digit_7(n: int) -> int:
    """
    Count the number of times the digit 7 appears in a given integer.
    
    Args:
        n (int): The number to count digit 7 in.
    
    Returns:
        int: The number of times the digit 7 appears in n.
    """
    return str(n).count('7')


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit for the range of numbers to check.
    
    Returns:
        int: The number of times the digit 7 appears in numbers divisible by 11 or 13 and less than n.
    """
    count = 0
    for i in range(11, n):  # start from 11 since we need numbers divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_7(i)
    return count


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # 0
    print(fizz_buzz(78))  # 2
    print(fizz_buzz(79))  # 3
```

This script first defines a helper function `count_digit_7` to count the occurrences of the digit 7 in a given integer. It then defines the main function `fizz_buzz` to sum up these counts for numbers in the specified range. The test cases at the end verify the correctness of the implementation.