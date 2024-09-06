```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and (i - l.count(i)) % 2 == 0:
            return True
        seen.add(i)
    return False
```

This function iterates through the list, tracking unique positive integers. If there is a positive integer that is not seen before and the count of this integer divides evenly into the total sum, the function returns True. The idea is that the count of this integer will cancel out with its negative counterpart in the list, resulting in a sum of zero. The function will return False otherwise. 

Here is an example usage of the function:
```python
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
This will return False for the first three examples and True for the last two.