```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    
    for num, count in dups.items():
        if count > 1:
            return False
    
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
This function first checks if there are any elements in the list that appear more than once, using a dictionary to count the occurrences of each element. If there are any such elements, it returns False immediately since the condition of having duplicates and being sorted is not met. Otherwise, it proceeds to check if the list is sorted by iterating through the list and comparing each element with the next one. The `all()` function is used to check if all comparisons are true, which indicates a sorted list. If all comparisons are true, the function returns True, indicating that the list is sorted with no duplicates. 

Here is a simple test suite that can be used to validate the function:
```python
def test_is_sorted():
    # Basic cases
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

    # Edge cases
    assert is_sorted([5]) == True
    assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8]) == True

    # Cases with duplicates
    assert is_sorted([1, 2, 3, 4, 5, 6, 7, 1]) == False
    assert is_sorted([1, 2, 2, 3, 3, 4, 1]) == False
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False

test_is_sorted()
```
This test suite covers a variety of scenarios, including basic edge cases, to verify the correctness of the `is_sorted` function.