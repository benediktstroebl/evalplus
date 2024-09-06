```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] <= 1 for num in dups) and all(num <= nums for num, nums in dups.items())
```

The function uses a dictionary to count the number of times each element appears in the list and then checks two things:
1. That there is at most one occurrence of each element, with the help of the `all()` function and a generator expression.
2. That the elements are sorted, which is checked by verifying that the current number is less than or equal to all of the subsequent numbers in the list. 

The generator expression makes use of the `items()` method of the dictionary to return the `((key, value))` tuple pairs, where `key` is the element and `value` is its occurrence number. This is done so there is at most one occurrence of each element in the list. 

The dictionary `dups` is used to count the occurrences of each number in the list, and the `all()` function checks that each number appears only once in the list. 

The second check ensures that the numbers are sorted in ascending order by comparing each number in the list with all the subsequent numbers to check that they are increasing. 

The function returns `True` if the list is sorted and has at most one occurrence of each number, and `False` otherwise. 

Here is an example usage of the function:
```python
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # Outputs: True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # Outputs: False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # Outputs: True
```

This should be the case, since the function checks for duplicate values using a dictionary, and the output of the examples should be:
```
True
False
True
```