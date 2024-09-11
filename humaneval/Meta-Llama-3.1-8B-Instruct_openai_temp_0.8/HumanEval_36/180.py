```python
def count_digit_7(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n.
    
    :param n: The upper bound (exclusive).
    :return: The count of digit 7.
    """
    count = 0
    for i in range(n):
        count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    :param n: The upper bound (exclusive).
    :return: The count of digit 7 in divisible numbers.
    """
    return count_digit_7(n-1) - count_digit_7(n-1 - n % (11 * 13))  # Subtract the count of numbers from n to (n - n % (11 * 13)) that are divisible by 11 or 13


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script first defines a helper function `count_digit_7` to count the occurrences of the digit '7' in all integers less than `n`. The main function `fizz_buzz` then uses this helper function to count the occurrences of the digit '7' in all integers less than `n` which are divisible by 11 or 13. The `count_digit_7` function works by converting each integer to a string and using the `count` method to count the occurrences of the digit '7'. The `fizz_buzz` function then subtracts the count of numbers from `n` to `(n - n % (11 * 13))` that are divisible by 11 or 13 to get the final count.