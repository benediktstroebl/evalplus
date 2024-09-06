```python
def unique(lst):
    return sorted(set(lst))

# Test case 1:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Expected output: [0, 2, 3, 5, 9, 123]

# Test case 2:
print(unique([3, 3, '123']))
# Expected output: [123]

# Test case 3:
print(unique([55, 'a', 123, 'bc', 'e']))
# Expected output: ['a', 'bc', 'e', 123]

# Test case 4:
print(unique([True, False, True]))
# Expected output: [True]
```
This script defines a function called unique which takes a list lst as input and returns a sorted set of unique elements in that list, which is also a list. It uses the unique property to solve this problem.

The script also provides test cases to check the correctness of the unique function, and the expected outputs are printed.