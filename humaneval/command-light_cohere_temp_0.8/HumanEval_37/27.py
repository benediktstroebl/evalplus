```python
def sort_even(lst):
    return lst[:] if all(x % 2 == 0 for x in lst) else lst

# Test cases for the function
test_sort_even = [
    [5, 6, 3, 4],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

test_sort_even_res = sort_even(test_sort_even)
print("Test cases:", end="")
for item, expect in zip(test_sort_even_res, test_sort_even):
    print(f"{item} = {expect}, should be sorted as [3, 4, 5, 6]")
```