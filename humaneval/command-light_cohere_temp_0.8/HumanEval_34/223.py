```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

#Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))  # expected output: [0, 2, 3, 5, 9, 123]

#Test case 2
test_case2 = [7, 8, 6, 5, 9, 10]
print(unique(test_case2))  # expected output: []

#Test case 3
test_case3 = [1, 2, 3, 4, 5, 6, 7]
print(unique(test_case3))  # expected output: [1, 2, 3, 4, 5, 6]
```
This Python function unique takes a list as input and returns a new list containing only the unique elements that are not present in the initial list and [0]. The function utilizes the set data type to keep track of elements that have already been seen, ensuring the uniqueness of the output. This self- result is unique list.