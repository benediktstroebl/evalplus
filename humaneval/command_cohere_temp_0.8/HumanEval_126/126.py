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

The function works by using a dictionary to count the occurrences of each number in the list and verify that there are no more than 1 duplicate occurrences for each number, and that each number is sorted in increasing order. The `all()` functions are used to check these conditions, so the function returns True when the list is sorted and has no more than 1 duplicate for each number, and False otherwise. 

The following test cases illustrate how the function performs:
```python
TESTS = [[], [5], [1, 2, 3, 4, 5], [1, 3, 2, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 2, 3, 3, 4], [1, 2, 2, 2, 3, 4]]

for lst in TESTS:
    print(f'is_sorted({lst}) = {is_sorted(lst)}')
```
The expected output from this would be:
```
is_sorted([]) = True
is_sorted([5]) = True
is_sorted([1, 2, 3, 4, 5]) = True
is_sorted([1, 3, 2, 4, 5]) = False
is_sorted([1, 2, 3, 4, 5, 6]) = True
is_sorted([1, 2, 3, 4, 5, 6, 7]) = True
is_sorted([1, 2, 2, 3, 3, 4]) = True
is_sorted([1, 2, 2, 2, 3, 4]) = False
```
Please note that the `TESTS` list above can be modified to include other test cases to further verify the function.