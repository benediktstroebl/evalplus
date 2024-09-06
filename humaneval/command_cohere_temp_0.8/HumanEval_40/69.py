```python
def triples_sum_to_zero(lst):
    # Using sorting to simplify the task
    lst.sort()
    for i in range(len(lst) - 2):
        if lst[i] + lst[i + 1] + lst[i + 2] == 0:
            return True
    return False
```

This function takes a list of integers, `lst`, as its argument and returns `True` if the list contains three elements that sum up to zero and `False` otherwise. The code checks if any two adjacent elements in the sorted list sum up to the value of the third element. It returns `True` if any such triplet is found and `False` otherwise. 

Here is an example usage of the function:
```python
print(triples_sum_to_zero([1, 3, 5, 0]))  # False
print(triples_sum_to_zero([1, 3, -2, 1]))  # True
print(triples_sum_to_zero([1, 2, 3, 7]))  # False
print(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))  # True
print(triples_sum_to_zero([1]))  # False
```

This should output:
```
False
True
False
True
False
```

This code is efficient, taking `O(n log n)` time, where `n` is the length of the input list, as it only requires sorting the list once and performing adjacent element checks.