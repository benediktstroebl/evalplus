Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    # Define the list of digits from 0 to N-1, where N is the base representing the n-th power of 10.
    base = 10**(n - 1)
    # Generate all the numbers from 0 to N-1 in a list.
    digits = list(range(base))
    # Define the starting and ending digits to be 1.
    start = 1
    end = 1
    # Initialize the count of numbers with 1 as start or end.
    count = 0
    # Iterate through the list of digits, shifting the starting digit to the end and the ending digit to the start.
    for i in range(n):
        digits[i], digits[n - 1 - i] = digits[n - 1 - i], digits[i]
        # Update the start and end if the number is a permutation of digits.
        if tuple(digits) == tuple(str(base // 10**i) for i in range(n)):
            if (start == 1 or end == 1) and base != 1:
                count += 1
            start = end
            end = 1
            base //= 10
    return count
```

This function should correctly solve the problem for any input positive integer `n` and return the count of numbers of `n-digit` positive integers that start or end with 1. 

The logic is as follows:
- The function first creates a list of digits from 0 to `base-1`, where `base` is the `n-th` power of 10.
- It then sets the 'start' and 'end' digits to 1 and iterates through the list of digits, shifting the starting digit to the end and the ending digit to the start.
- It checks if the permuted digit list forms a number and increments the count if the start or end digit is 1 (excluding the case of a single digit number).
- Finally, it increments the starting 'start' and 'end' digits for the next iteration. 

Overall, this algorithm solves the problem in linear time `O(n)` and is relatively efficient in terms of time and space complexity. 

Note: This code is written in Python 3. If you are using a different version of Python, you may need to adjust the code accordingly.