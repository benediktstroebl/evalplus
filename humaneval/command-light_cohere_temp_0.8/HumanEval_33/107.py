```python
def sort_third(l: list):
    """Sorts a list l such that values not divisible by three are at the beginning, and
    values divisible by three are at the end. The list is modified in-place."""
    for i in range(len(l)):
        if l[i] % 3 != 0:
            l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
           
    return l

# Test the function with various inputs
test_list = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(test_list)
print("Sorted list:", result)

# Test with a list of strings
string_list = ["Python", "is", "Bad", "programming"]
result = sort_third(string_list)
print("Sorted list of strings:", result)

# Test with a list of mixed data
mixed_list = [1, 2, 5, 6, 3, 7]
result = sort_third(mixed_list)
print("Sorted list of mixed data:", result)
```
The function `sort_third` takes a list `l` as input and returns a list `l` where the elements that are not divisible by three are moved to the beginning, and the elements that are divisible by three are moved to the end of the list.