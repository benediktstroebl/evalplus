```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and pairs_sum_to_zero(l, i, seen) == True:
            return True
        seen.add(i)
    return False

def pairs_sum_to_zero(l, x, seen):
    # Write your code here
    if x == 0:
        return True
    if x < 0:
        return pairs_sum_to_zero(l, -x, seen)
    return pairs_sum_to_zero(l, x - 1, seen) or pairs_sum_to_zero(l, x + 1, seen)
```

The approach uses a recursive method to solve the problem, starting with a positive integer `x` and checking if `x` equals 0. If it does, then we have found a pair that sums up to 0. If `x` is less than 0, we revert to the positive `x` and try to find a pair that would sum to `x`. We also try to find pairs that sum up to `x - 1` and `x + 1` as part of the process. 

The base case occurs when we deal with a negative number in some nested calls, at which point we return True signaling that we have found a valid pair. The initial function `pairs_sum_to_zero` sets up the process and kicks off the recursive call with a positive `x`. 

The unit tests provided challenge the function with lists of different integer combinations, including a special test case of a list with only one integer.  This recursive approach has a time complexity of `O(2^n)` due to the repeated division of the problem into two sub-problems, and a space complexity of `O(n)` due to the need to keep track of the seen elements.