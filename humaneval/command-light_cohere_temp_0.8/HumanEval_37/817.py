```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return sorted(l,key=lambda x:x if x%2 else x+1)
# Example usage
test_list = [1,2,3]
result = sort_even(test_list)
print(result)
``` 
The output of the above code is: 
```
[1, 2, 3]
``` 
This script defines a function sort_even that takes a list l as input and returns a sorted list l'. The function uses the sorted() function with a custom key function that returns the index of the item if it's even, and returns the item if it's odd.  The the key is a lambda function that returns the index of the item if it's even, and returns the item if it's odd. The sorted() function sorts the result list based on the custom key function, and returns the sorted list.