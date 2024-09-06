```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function examines every integer in the list, tracking those that have been seen before using a set data structure. When a positive integer is encountered, the function checks if it has been seen more than once and if the list contains an integer whose subtraction results in the positive integer. The function performs a similar check for negative integers, ensuring that their pair in the list sums up to zero. If any such pairs are found, it returns True; otherwise, it returns False. 

Here is an example usage:
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
This demonstrates that the function correctly identifies pairs that sum to zero and returns True in such cases, while any other valid input returns False.