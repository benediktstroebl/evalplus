Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Generate all n-digit numbers where the leading digit (start) cannot be 0, and the trailing digit (end) is optional
    numbers = [str(i) for i in range(1, 10)**n]
    
    # Count numbers that start or end with 1
    return sum(1 for num in numbers if num[0] == '1' or num[-1] == '1')
```

This script defines the `starts_one_ends` function, which takes a positive integer `n` as input and returns the count of `n-digit` positive integers that start or end with 1. It accomplishes this by generating all valid `n-digit` numbers using a list comprehension and then counting how many of them start with 1 or end with 1 using a generator expression.

Let's break down the code step by step:
1. **Function Definition**:
   ```python
   def starts_one_ends(n):
   ```
   Here, we define the function `starts_one_ends` that takes a single argument `n`, which represents the number of digits in the positive integers we want to count.

2. **Number Generation**:
   ```python
   numbers = [str(i) for i in range(1, 10**n)]
   ```
   To solve the problem, we need to count the numbers of `n-digit` positive integers that start or end with 1. We generate all valid `n-digit` numbers using a list comprehension. Here's how it works:
     - `str(i)`: We convert each integer `i` to a string representation.
     - `range(1, 10**n)`: We create a range of numbers from 1 to `10^n` (inclusive of 10^n). This ensures we cover all possible digits for `n-digit` numbers.
     - `for i in range(1, 10**n)`: We iterate over each number from 1 to `10^n` and convert them to strings.

3. **Counting Valid Numbers**:
   ```python
   return sum(1 for num in numbers if num[0] == '1' or num[-1] == '1')
   ```
   To count the numbers that start or end with 1, we use a generator expression. For each `num` in the `numbers` list, we check if the first digit (indexed at `num[0]`) is 1 or if the last digit (indexed at `num[-1]`) is 1. If either condition is true, we increment the count. Finally, we return the total count of valid numbers.

This script ensures that it covers all valid `n-digit` positive integers and counts the ones that satisfy the conditions specified in the problem statement.