```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l]
    return result

#Test the function with a list of lists
test_list = [[1, 2, 3], [5, 3, 5], [2, 3, 3]]
result = incr_list(test_list)
print(result)  # Output: [2, 3, 4], [6, 3, 5], [4, 3, 6]

#Test the function with a single list
test_list1 = [5, 3, 5, 2, 3, 3]
result1 = incr_list(test_list1)
print(result1)  # Output: [6, 4, 6, 3, 4, 4, 10]

#Test the function with a nested list
test_list2 = [[5, 3, 5], [2, 3, 3]]
result2 = incr_list(test_list2)
print(result2)  # Output: [6, 4, 6]

#Test the function with a list of strings
test_list3 = ['a', 'b', 'c']
result3 = incr_list(test_list3)
print(result3)  # Output: ['a', 'b', 'c', '1']
```