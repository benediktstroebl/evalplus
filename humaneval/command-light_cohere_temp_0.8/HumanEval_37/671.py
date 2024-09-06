```python
def sort_even(lst):
    even_set = set(lst[::index(lambda x: x % 2 == 0)::len(lst)::x for x in lst])
    return [::index(x) for x in lst if x in even_set]

# Test cases
test_list = [5, 6, 3, 4]
test_list_reverse = [4, 6, 3, 5]
test_empty = []

# Test results
print("Original list:", test_list)
print()
print("Sorted list:", sort_even(test_list))
print()
print("Original list reversed:", test_list_reverse)
print()
print("Sorted list reversed:", sort_even(test_list_reverse))
print()

# Test empty list
print("Sorted empty list:", sort_even([]))
```
The function **`sort_even`** takes a list and returns a new list with elements from the original list that are equal to the corresponding even index value in the original list, sorted in ascending order. 

The function uses the **`index`** function to get the index of the even elements in the list.