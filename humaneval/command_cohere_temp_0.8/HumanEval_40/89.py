```python
def triples_sum_to_zero(l: list):
    # Write your code here. Read the instructions carefully till the end!</br>
    seen = set()
    for a, b in itertools.combinations(l, 2):
        if a + b == 0 and (a, b) not in seen:
            seen.add((a, b))
            if len(seen) == 3:
                return True
    return False
```

**Instructions**:
1. The solution makes use of the `itertools.combinations` function to efficiently generate all possible pairs of elements in the input list `l`.
2. It uses a `set` called `seen` to keep track of the unique pairs that sum to zero. This is done to detect the presence of three distinct pairs that sum to zero.
3. The function returns `True` if three distinct pairs are found and `False` otherwise. 

**Complexity Analysis**:
The algorithm's time complexity is O(N^2), where N is the size of the input list `l`. This is because it checks all possible pairs of elements in the list. 

The space complexity is O(N) since it requires additional space to store the `seen` set for unique detection of the pairs.

This approach allows for a straightforward and efficient solution that achieves a time complexity of O(N^2) while maintaining a self-contained Python script.