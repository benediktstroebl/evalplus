```python
def unique(l: list):
    return list(set(l))

# Test case 1:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
``` 
This code defines a function unique that takes a list l as input and returns a list of unique elements from that list, using the set() function to get the unique elements and the list() function to convert the set into a list. 

The code then prints the set of unique elements in the list passed as test case 1.