```python
def strange_sort_list(lst):
    lst.sort() == sorted(lst, reverse=True)
    lst.sort() == sorted(lst)
    return sorted(lst)

# Test cases
test_strange_sort_list = [
    [],
    [1,4,2,3],
    [5,5,5],
]

# Function Calls
test_strange_sort_list[0]
# Test Case 1: [1,4,2,3] should return [1,4,2,3] in strange order
test_strange_sort_list[1]
# Test Case 2: [1,4,2,3] should return [1,4,2,3] in normal order
test_strange_sort_list[2]
# Test Case 3: [] should return []
test_strange_sort_list[3]
# Test Case 4: [5,5,5] should return [5,5,5] in strange order
test_strange_sort_list[4]
# Test Case 5: [] should return []
```