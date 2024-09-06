```python
def sort_even(lst):
    # Define the function
    even, odd = [], []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    
    # Return the even and odd lists
    even.sort()
    odd.sort()
    value = lambda a two: two[1] - two[0]
    even = [x for x in even if x%2 == 0]
    odd = [x for x in odd if x%2 == 1]
    
    # Return the sorted list
    return even
```