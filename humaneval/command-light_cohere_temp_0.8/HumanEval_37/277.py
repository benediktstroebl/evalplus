```python
def sort_even(lst):
    even_set = set(lst[1:])
    return [lst[0] if x == even_set.is_even(x) else x for x in lst]

def is_even(x):
    return x % 2 == 0

# Test the function
even_test = [1, 2, 3]
print(sort_even(even_test))
```