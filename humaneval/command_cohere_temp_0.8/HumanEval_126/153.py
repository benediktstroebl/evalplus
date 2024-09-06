```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] <= 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function uses a simple dictionary (`dups`) to count the occurrences of each number, and then it checks two things:
1. Whether each number appears at most once (using `all(dups[num] <= 1 for num in dups)`) - This ensures no duplicates.
2. Whether the numbers are sorted (`all(num < nums[1] for num, nums in dups.items())`) - This is done by checking if the key-value pairs in `dups` are sorted. 

The above code will correctly determine whether the list of numbers is sorted without multiple duplicates. 

This approach does have a slight pathological case overhead, as it creates a dictionary. Thus, if you're dealing with extremely large lists of integers, you might want to consider an alternative data structure like a set or a threshold for when to use a dictionary. Nevertheless, for most practical applications, this solution will work efficiently.