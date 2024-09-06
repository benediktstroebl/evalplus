Here is a self-contained Python script that defines a function unique that returns sorted unique elements in a list:
```python
def unique(lst):
    set(lst)=set(lst)
    return list(set())

# Test case 1:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# expected output: [0, 2, 3, 5, 9, 123]

# test case 2:
print(unique([123, 22, 45, 4, 67, 8, 22, 91, 81, 90] ))
# expected output: [22, 45, 4, 67, 81, 90]

# test case 3:
print(unique(['A','B','C']))
# expected output: ['A', 'B', 'C']

# test case 4:
print(unique(['a','bc','de','f']))
# expected output: ['a', 'bc', 'de', 'f']
```
This script defines a unique function that takes a list as input and returns a new list containing unique elements from the original list. The function uses the unique elements in the list using the set() function and the list() function to convert the set into a list. This ensures the set() does not create duplicates.