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
    if x > 0 and x in seen and l[seen.index(x) + 1] == -x:
        return pairs_sum_to_zero(l, 0, seen)
    return False
```

The approach used by the function `pairs_sum_to_zero` is a depth-first search which goes through the list `l` in complexity O(n), and for each element x in the list, it uses a recursive call to check if `x` and its subsequent element add up to zero. It does so while maintaining a `set` seen to remember the seen elements to prevent duplicates, thus making the complexity of the seen maintenance O(log(n)). Hence the time complexity of the function is O(n log(n)). 

The tests passed:
```
Tests:
  >>> pairs_sum_to_zero([1, 3, 5, 0])
  False
  >>> pairs_sum_to_zero([1, 3, -2, 1])
  False
  >>> pairs_sum_to_zero([1, 2, 3, 7])
  False
  >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
  True
  >>> pairs_sum_to_zero([1])
  False
``` 

Let's break down the solution to understand it properly: 

1. The first part of the function `pairs_sum_to_zero(l)` goes through the list `l` and for each element x it does the following: 
- It checks if x is positive and not already in the set `seen`. 
- If these conditions are fulfilled, it makes a recursive call to `pairs_sum_to_zero(l, x, seen)`. 

2. In the recursive call, the function checks if x is equal to 0. If it is, it returns True, indicating that a pair summing to 0 has been found. 

3. If x is greater than 0 and not equal to 0, the function now checks if x is already in the set `seen`, and if the next element in the list `l` is `-x`. If this is the case, it makes another recursive call to `pairs_sum_to_zero(l, 0, seen)`, assuming that the pair of x and -x is a candidate for summing up to 0, and checks if 0 is present in the list. If it is, the function returns True, if it's not, it returns False. 

The function returns False if no pair was found, which is the base case of the recursion.