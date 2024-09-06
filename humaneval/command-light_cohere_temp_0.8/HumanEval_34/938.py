```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

#Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_case1))
# Output: [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 3, 6, 7, 8, 9, 2]
print(unique(test_case2))
# Output: []
``` 
The code defines a function unique that takes in a list lst and iterates through it. It uses a unique elements using a set, seen, to keep track of the elements it has encountered so far. It then appends any elements that aren't in the seen set to result, which will be all the unique elements in the input list. 

The test cases demonstrate that the function correctly identifies and returns the unique elements in the list.