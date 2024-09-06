```python
def filter_integers(values): 
    """ Filter given list of any python values and return list of integers""" 
    return [x for x in values if isinstance(x, int)] 

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1) 
print(result1)  # Output: [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2) 
print(result2)  # Output: [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, {}]
result3 = filter_integers(values3) 
print(result3)  # Output: [1, 2, 3]
```
This script provides a function `filter_integers` that takes a list of values and returns a new list with only the integer values from the original input list. 
It uses a list comprehension to filter out the integers from the input list.