```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown code block for hints or the full solution.
    # Returned value structure:
    # True if lst has three distinct elements that sum to zero, False otherwise
    seen = set()
    for a in lst:
        if a < 0:
            continue
        for b in lst:
            if b < 0 or b == a:
                continue
            for c in lst:
                if c < 0 or c == a or c == b:
                    continue
                if a + b + c == 0 and a not in seen and b not in seen and c not in seen:
                    seen.add(a)
                    seen.add(b)
                    seen.add(c)
                    return True
    return False
```

#### Explanation:
The code uses a set called `seen` to keep track of already-seen elements to ensure the result involves only three distinct elements. The algorithm tries all possible combinations of lst using three nested loops. 

Being careful with negations, the code checks if the summation of the three chosen elements equals zero and none of them are the same. If so, it returns True, and False otherwise. 

The code is efficient since the number of loops is proportional to the square of the size of the input list, which is `O(n^2)`. However, it also reduces unnecessary loops by ignoring negative elements, which wouldn't contribute to a sum of zero. 

To save time, you can set a maximum iteration limit for the loops, which would make this function operate in polynomial time, specifically O(n^2^k), where k is the maximum number of iterations.