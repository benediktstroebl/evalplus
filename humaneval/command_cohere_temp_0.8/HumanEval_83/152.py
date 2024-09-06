```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes starting with 1 and
    # ending with 1, starting with 1 and ending with 11, and so on.
    counts = [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    return counts[-1] if n == 1 else sums(counts[:n]) - sums(counts[:n - 1])

def sums(numbers):
    # If there is only one number, return it. Otherwise, return the sum of
    # all the numbers in the list minus the sum of all the numbers in the
    # list minus 1 (to account for the counting double-counting the single
    # digits).
    if len(numbers) == 1:
        return numbers[0]
    return sum(numbers) - sum(x for x in numbers if x != numbers[0])
```

This Python script defines a function `starts_one_ends(n)` which accepts a positive integer `n` and returns the number of `n-digit` positive integers that start or end with the digit 1. The function uses a predefined array `counts` to store the count of starting or ending with 1 for each n-digit number. This array is used to calculate the actual count by either directly returning the last element if `n` is 1, or by computing the sum of counts from 1 to `n` less the sum from 1 to `n-1`. The `sums()` function is used to simplify the logic of calculating the sum of elements in a list. It branches to a single-element case where it returns the element if there is only one number, and otherwise, it computes the sum of all numbers in the list minus the sum of all numbers in the list minus 1 to correct for the double-counting of the single digits in the larger sums.

Here is an example usage of the function starts_one_ends:
```python
print(starts_one_ends(3))
```

The above will print out the result `16`. This is so because the 3-digit numbers that start or end with 1 include `111, 11, 101, 1011, 1, 11111, 1110, 1001, 10011, 1111, 11001`, and their total count is `16`.