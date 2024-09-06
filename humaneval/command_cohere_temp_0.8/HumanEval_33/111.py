```python
def sort_third(input_list):
    result = []
    for i in input_list:
        if i % 3 == 0:
            result.append(sorted(input_list[i]))
        else:
            result.append(input_list[i])
    return result
    
# Tests:
assert sort_third([1, 2, 3]) == [1, 2, 3]
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
```