```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 9
    else: 
        return (10 ** (n - 1)) * 2 - 9
```
The function kicks off with edge case handling for n < 1 and if n == 1 returns 9 respectively. For values of n > 1, it takes advantage of the fact that each digit position can be filled in with a 1 only once, either as a starting digit or an ending one, as desired. It employs the formula `(10 ** (n - 1)) * 2 - 9` for the count, which considers all possible permutations of the digits (excluding 1111...1) and subtracts the counts of the numbers that end in 1 as these are counted twice, once for starting and once for ending. This undercounts by 1 which is corrected by +1 at the end.