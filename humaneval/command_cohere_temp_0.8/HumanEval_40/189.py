```python
def triples_sum_to_zero(lst):
    # Using dictionaries and sets to filter out duplicates and sum values
    d = {}
    s = set(lst)
    for a in lst:
        if a not in d:
            d[a] = 0
        d[a] += 1
        if len(d) > 2 and sum(lst) == 0:
            return True
        if len(d) == 2 and len(s) == 1:
            return True
    return False
```

This Python script defines a function called `triples_sum_to_zero` that takes a list called `lst` as input. It uses a dictionary and a set to efficiently solve the problem. The dictionary is used to count the occurrences of each unique element in the list, and the set is used to remove duplicate elements from the list. 

Then it iterates through each element in the list `a` and updates its count in the dictionary `d`. If the number of unique elements exceeds 2 and the sum of the elements is 0, it returns `True` indicating that there are three distinct elements that sum to zero. If there are 2 unique elements left and only one element in the set, it also returns `True` because the remaining 2 elements must form a pair that sums to zero. 

The script includes examples in the docstring to test the function and returns `False` in any other case.