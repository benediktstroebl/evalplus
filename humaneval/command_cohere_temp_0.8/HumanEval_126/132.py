```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function employs two conditions to determine list sorting:
1. All elements are unique, confirmed by checking if the count of duplicates is strictly 1 for all elements.
2. The list is sorted, confirmed by checking if the subsequent number of every element is greater than the previous one. 

The all function is used in conjunction with the lambda functions to determine if all elements satisfy these two conditions. 

This approach allows the code to determine sorting without using any built-in sorting functions, thus preserving uniqueness. 

The code is concise and efficacious, delivering the sorting verdict for the given list. 

The unit tests can be incorporated to assess the function's effectiveness on various input lists. Example usage in the main function can also be incorporated to test the function on real-world examples. 

Here is an example of how to use the is_sorted function:
```python
my_list = [1, 2, 3, 4, 5, 6, 7]
if is_sorted(my_list):
    print("The list is sorted in ascending order without duplicate elements.")
else:
    print("The list is not sorted in ascending order or contains duplicate elements.")
```

And the corresponding test suite:
```python
def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
    assert is_sorted([5]) == True
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True
```