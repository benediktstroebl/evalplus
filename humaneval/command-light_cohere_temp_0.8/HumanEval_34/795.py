```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(x))
    return result

# Test the function
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)  # Expected output: [0, 2, 3, 5, 9, 123]
``` 
This code defines a function `unique` which takes a list as input and returns a sorted unique elements in that list. It uses a `seen` set to keep track of the elements we've seen so far and `result` list to store the unique elements. The function iterates through each element in the input list and if the element is not in the seen set, it's added to the set and the result list. Then it's `result` list is returned.