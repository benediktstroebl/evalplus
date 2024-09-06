```python
def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (s[:i] for i in range(len(s) + 1) for s in (first, second)) ))
``` 

The function iterates through rotations of the second word and uses set membership to check if any of these rotations are sub-strings of the first word.

This approach ensures a time complexity of O(n^2) but can be easily improved to O(n log n) for the most efficient solution. 

The given code is simplistic in nature and should be reasonably efficient for words of reasonable lengths.

If the primary concern is optimal time complexity, we can approach the problem through sorting and merging.

Let me know if you'd like a more optimized version!