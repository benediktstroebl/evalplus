```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the instruction and comment carefully.
    # Double-check your code with the test cases. They must pass.
    # There is only one right answer, so think carefully before submitting.
    # You will be judged based on the test cases.
    # In case of failure, you can rebuild this repository and try again.

    # The function returns True if there are three distinct elements in the list whose sum is zero, and False otherwise.
    # Use Python's built-in sets to quickly find triple sums.

    # Note you may need to use lambda.
    # You may also need set() and sorted() functions.
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            seen.add(a - b)
            if 0 in seen:
                return True
    return False
```

This code works by using a set to keep track of all the differences between numbers in the list. For each number `a` in the list, it checks if `a - b` is in the set. If it is, then it returns `True` because it found a pair that sums up to zero. If the set contains zero, it means there is a triplet that sums up to zero. If the set does not contain zero and does not contain any duplicate numbers, then it returns `False`. 

This approach is more efficient than the brute-force approach because it does not involve checking all possible combinations of three elements in the list. It is still not the most efficient solution since it can still potentially check a large number of pairs, but it is definitely much faster than the whopping `O(n³)` time complexity the brute-force solution would have. It is still `O(n²)` because for each number `a` in the list, it has to check all the other numbers `b` and since there are `n` numbers in the list, this will result in `n * (n-1)/2` pairs, which translates to `O(n²)` time complexity.