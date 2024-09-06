```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in terms of value but ordered without divisors of three."""
    new_list = []
    for num in lst:
        if num % 3 == 0:
            new_list.append(num)
   
    new_list.append(num)
   
    return new_list

# Test the function
new_list = sort_third([1, 2, 3])
print(new_list) 
```