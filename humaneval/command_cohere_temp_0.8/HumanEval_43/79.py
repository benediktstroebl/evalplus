```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if (-x) in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through every element in the list and simply checks if the given number has a pair that can sum up to zero. It stores the encountered numbers in a set so that we can check if a number has already appeared before. If there are two appearances of the number in the list, only then it returns True, else it returns False. 

This solution has a time complexity of O(n^2) due to the nested loop structure, but it has a relatively intuitive approach that is straightforward to implement.