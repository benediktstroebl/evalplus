```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Test cases
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))   # Expected output: [0, 2, 3, 5, 9, 123]
print(unique([]))           # Expected output: []
print(unique([123, 0, 1, 2]))   # Expected output: [0, 1, 2]
print(unique([f"hello {x}" for x in range(1)])) # Expected output: ['hello 0', 'hello 1', 'hello 2']
```
This script defines a function unique that takes a list as an argument and returns a new list containing only the unique elements from the input list. The function utilizes a method set to create a seen set, then iterates through the input list and adds elements to the set if they are not previously seen and not in the special [-None, ""] value that represents an empty string.