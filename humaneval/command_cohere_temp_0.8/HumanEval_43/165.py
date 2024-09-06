```python
def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            if i in seen and l.count(i) > 1:
                return True
            seen.add(i)
        else:
            if -i in seen and l.count(-i) > 1:
                return True
            seen.add(-i)
    return False
```

This Python script defines a function pairs_sum_to_zero that takes a list l as input. It aims to determine whether there are two distinct elements in the list whose sum equals zero. The function iterates through the list, tracking elements visited using a set called seen.

For positive elements i, it checks if i is already in the seen set. If so, the function checks if there are more than one occurrence of i in the list. This indicates the presence of another element that can complement i to sum up to zero.

For negative elements -i, it follows the same logic, but uses the complement of i (-i) to search in the seen set. If -i is found, and there are multiple occurrences of it, the condition is satisfied.

The function returns True if such pairs are found and False otherwise. This method ensures efficiency and adheres to the problem requirement of checking for pairs that sum up to zero.