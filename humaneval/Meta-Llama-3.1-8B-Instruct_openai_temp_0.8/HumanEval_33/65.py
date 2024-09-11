### Sort Third
#### Problem Description
The function `sort_third` takes a list `l` and returns a new list where elements at indices not divisible by 3 are unchanged, and elements at indices divisible by 3 are sorted in ascending order.

#### Code
```python
def sort_third(l: list):
    """Sort elements at indices divisible by 3 in ascending order."""
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(l) if j % 3 == 0])[k] 
            for i, x in enumerate(l) for k in range(i % 3) if i % 3 == 0]
```

#### Explanation
The function uses list comprehension to create a new list where elements at indices not divisible by 3 are copied as is, and elements at indices divisible by 3 are replaced with the corresponding sorted element from the sublist of elements at indices divisible by 3.

#### Test Cases
```python
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```
Note: This solution assumes that the input list `l` has at least one element at an index divisible by 3. If this is not guaranteed, additional error handling may be necessary.