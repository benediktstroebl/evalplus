```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) % 2 == 0)

# Test the function with sample inputs
list1 = [1, 2, 3]
list2 = [5, 6, 3, 4]

# Call the function and assign the result to a variable
sorted_list1 = sort_even(list1)
sorted_list2 = sort_even(list2)

# Compare the sorted lists
print("List1 sorted:", sorted_list1)
print("List2 sorted:", sorted_list2)

```

The output of this code will display the sorted lists according to even items. The print statement will show that the second list is sorted in the same way as the first list.

So, the output will be:
```
List1 sorted: [1, 2, 3]
List2 sorted: [3, 6, 5, 4]
```