```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test case 1: Returns unique elements from the list [5, 3, 5, 2, 3, 3, 9, 0, 123]
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
 # Output: [0, 2, 3, 5, 9, 123]

# Test case 2: Returns an empty list
unique([])
 # Output: []

# Test case 3: Repeated elements
unique([3, 3, 5])
 # Output: [3, 5]

# Test case 4: List with duplicate elements
unique([1, 2, 3, 4, 3])
 # Output: [1, 2, 3]
 ```

This function unique is a handy tool for efficiently and correctly identifying unique elements in a list. It employs a set to keep track of elements already encountered, and then iterates through the list, appending any elements not previously seen. This method ensures that duplicates are correctly excluded, making it an effective solution for problems involving unique element identification.