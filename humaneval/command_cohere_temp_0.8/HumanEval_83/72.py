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
        # Split counts into those that start with 1 and those that end with 1.
        start_count = (n - 1) // 2
        end_start_count = (n - 1) // 2 + 1
        total = start_count + end_start_count
        return total
```
The logic behind the solution is based on the following:
1. When `n` is 1, there is only one possible number (`11`).
2. When `n` is even, it's possible to have `n`-digit numbers that start with 1 and also end with 1 (e.g., `1234567` where `2` and `7` are fixed digits). There's also a symmetric case for numbers starting with 1 - `1` and ending with `1`. Thus, the count is twice the count of digits, minus 1 (i.e., `(n-1)/2 + (n-1)/2 + 1`.
3. When `n` is odd, there are no numbers that end with 1 (as digits are ordered left-to-right in integers). The count is only for those starting with 1, so it's equal to `(n-1)/2`.

The function checks for `n` being less than 1, wherein it returns 0, and if `n` is equal to 1, it returns 1. For `n` greater than 1, it calculates the counts as explained and adds them up.