Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the prompt:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Create a count list to store the counts of numbers starting or ending with 1.
    count = [0] * (n + 1)
    # Initialize the count of numbers starting or ending with 1 to the numbers from 1 to n.
    for num in range(1, n + 1):
        # For numbers with a length of 1 to n, increment the count if the number starts or ends with 1.
        if num % 10 == 1:
            count[num] += 1
    # Return the final count of numbers starting or ending with 1.
    return count[1] + count[n]
```

This script provides the function `starts_one_ends` that takes a positive integer `n` as input and returns the count of `n-digit positive integers` that start or end with 1. The function uses a counting technique to track the count of numbers that start or end with 1, and then returns the sum of these counts for numbers with a single digit and numbers with `n` digits. This solution is efficient and provides the requested count for the given input. Let's break down the solution and explain each step:
1. **Function Definition**:
   ```python
   def starts_one_ends(n):
       """
       Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
       """
   ```
   This part defines the function `starts_one_ends` that takes a single argument `n`, which represents the length of the numbers we want to count. The docstring provides a clear explanation of the problem.
2. **Count Array Initialization**:
   ```python
   count = [0] * (n + 1)
   ```
   Here, we create an array `count` of size `(n + 1)` to store the counts of numbers starting or ending with 1. Each element `count[i]` will represent the count of numbers with `i` digits that start or end with 1. Initially, all elements are set to 0.
3. **Count Accumulation**:
   ```python
   for num in range(1, n + 1):
       if num % 10 == 1:
           count[num] += 1
   ```
   This loop iterates over the numbers from `1` to `n`. For each number `num`, it checks if the digit at the unit place is `1`. If it is, it increments the count of numbers starting or ending with 1 for that particular length `num` in the `count` array.
4. **Result Calculation**:
   ```python
   return count[1] + count[n]
   ```
   After the loop, the function returns the sum of counts of numbers that start or end with 1. The sum is calculated by adding the counts of numbers with a single digit (`count[1]`) and numbers with `n` digits (`count[n]`). The former includes numbers starting with 1 (e.g., 11, 12, ...) and numbers ending with 1 (e.g., 91, 92, ...), while the latter includes numbers starting with 1 (e.g., 1011, 1111, ...) and numbers ending with 1 (e.g., 9111, 9121, ...).

The function efficiently solves the problem within linear time `O(n)` and provides the count of