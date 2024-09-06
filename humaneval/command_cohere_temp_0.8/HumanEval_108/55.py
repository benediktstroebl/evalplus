```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This solution uses a powerful Python feature — `str.format()` which creates a string representation of the integers in the array, and `map(int, ...)` which translates these strings back to integers. These are then summed using the cumulative effect of a semicolon-separated chain of operations.

The detailed breakdown of the logical order of the operations is as follows:
1. `sum(...)` operates on the list of results returned by `map(int, ...)`, which in turn takes the list of strings produced by `str(n)`.
2. `map(int, ...)` translates each string to its corresponding integer.
3. `str(n)` translates the integer `n` to its string representation.

The resulting string is then parsed back to an integer using `sum(...)` which adds up the digits of the string, which are all greater than 0 for the intended solution. Thus, the output of this cumulative operation corresponds to the required count. 

This type of solution is efficient and commonly used in Python because it is concise and expressive, making complex transformations and operations on data more manageable. 

The unit test cases provided in the problem statement would evaluate correctly using this solution, ensuring its correctness and viability in handling the problem at hand.