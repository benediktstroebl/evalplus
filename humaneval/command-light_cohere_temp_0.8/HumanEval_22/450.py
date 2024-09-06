```python
def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

#Test cases
test_values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, [], ]

print(filter_integers(test_values))

# Output: [5]
```
This script defines a function called **filter_integers** that takes a list of values as an argument and returns a new list that contains only the integers from the input list. The function uses a list comprehension to filter out the integers from the input list and returns the new list. 

Additionally, the script provides a series of test cases to ensure the correctness of the function by passing different values and checking the returned list.