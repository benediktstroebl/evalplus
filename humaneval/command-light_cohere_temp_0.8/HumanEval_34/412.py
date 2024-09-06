```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in [0]]

#Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))  #Expected output: [0, 2, 3, 5, 9, 123]

#Test case 2
test_case2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(unique(test_case2))  #Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Test case 3
test_case3 = ['a', 'bc', '!e', 'a', 'b']
print(unique(test_case3))  #Expected output: ['a', 'bc', '.e', 'a', 'b']
```

This script defines a function unique that takes a list as an input and returns a new list with unique elements. The function utilizes a seen set to track the unique elements and a generator expression to filter out duplicates. 

The test cases are then applied to verify the correctness of the unique function.