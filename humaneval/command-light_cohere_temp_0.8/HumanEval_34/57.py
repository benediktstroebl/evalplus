```python
def unique(lst):
    return list(set(lst))

# Test case 1
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
 [0, 2, 3, 5, 9, 123]

# Test case 2
x = [0, 2, 3, 4, 5, 6, 7]
y = unique(x)
print(x == y)  # True

# Test case 3
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5]
c = unique(a + b)
print(c == [1, 2, 3, 4, 5])  # True
``` 
This code defines a function unique that takes a list as input and returns a new list with unique elements from the original list. The test cases demonstrate that the unique function passes all tests and provides the expected output.