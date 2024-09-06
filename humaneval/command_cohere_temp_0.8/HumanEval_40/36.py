```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y > 0 and j != i + 1 and (j, x, y) not in seen:
                    seen.add((j, x, y))
                    if l[k] > 0 and j != k and k != i and (x, y, l[k]) not in seen:
                        return True
                        seen.add((x, y, l[k]))
                        break
                if j == len(l) - 1:
                    if x + y > 0 and (x, y, 0) not in seen:
                        return True
                        seen.add((x, y, 0))
    return False
``` 

Here is a brief explanation:
1. The code uses a set called 'seen' to keep track of already detected pairs to avoid duplicates and to ensure all three elements are distinct.
2. It then iterates the list twice to try finding the third distinct element that can sum up to zero with the first two.
3. A break statement is used to stop the second iteration to avoid unnecessary checks.
4. It also adds the third element to the 'seen' set to take care of the uniqueness.

This algorithm has a time complexity of O(n^2) with a space complexity of O(n) where 'n' is the length of the input list.