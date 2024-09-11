```markdown
### Fizz Buzz Problem Solution

#### Problem Description

Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

#### Solution

```python
def count_digit(n: int) -> int:
    """
    Helper function to count the occurrences of a digit in a number.
    
    Args:
    n (int): The number to count the digit in.
    
    Returns:
    int: The number of times the digit appears in n.
    """
    count = 0
    for digit in str(n):
        if digit == '7':
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit.
    
    Returns:
    int: The number of times 7 appears in the specified numbers.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit(i)
    return count


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

### Explanation

1. The `count_digit` function takes an integer `n` and returns the number of times the digit 7 appears in `n`.
2. The `fizz_buzz` function iterates over integers from 1 to `n-1` (inclusive).
3. For each number, it checks if the number is divisible by 11 or 13 using the modulo operator (`%`).
4. If the number is divisible, it counts the occurrences of the digit 7 in that number using the `count_digit` function and adds the count to the total.
5. Finally, it returns the total count.

### Time Complexity

The time complexity of this solution is O(n log n) due to the conversion of numbers to strings in the `count_digit` function. This is because string operations are typically O(n) where n is the length of the string. The loop in the `fizz_buzz` function iterates over n-1 numbers, resulting in a time complexity of O(n log n).