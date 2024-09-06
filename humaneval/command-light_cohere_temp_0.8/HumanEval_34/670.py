```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not ]

# Test the function
[5, 3, 5, 2, 3, 3, 9, 0, 123].unique() == [0, 2, 3, 5, 9, 123]
 ``` 
This function unique takes a list lst as an argument and creates a set seen to keep track of elements already encountered. Then, it iterates through each element in the list and adds it to seen if it is not in there yet and not previously encountered. The function returns a unique list containing only the elements from the original list that are not in the set seen. 

Would you like help implementing any other code?