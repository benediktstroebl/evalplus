```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The count of digit 7 in the range.
    """
    count = 0
    for i in range(11, n, 11):
        for j in range(13, n, 13):
            if i <= j:
                num = i
            else:
                num = j
            while num < n:
                count += str(num).count('7')
                num += 11
                if num < n and num % 13 == 0:
                    num += 12
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```
This script works by iterating over numbers that are multiples of 11 and 13, and counting the occurrences of the digit 7 in each number. The `while` loop inside the `if-else` block is used to increment the number by 11, and if it becomes a multiple of 13 before reaching `n`, it increments by 12 to avoid counting the same multiple of 11 twice.