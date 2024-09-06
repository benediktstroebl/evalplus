```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
``` 

This Python script defines a function called `incr_list`. This function takes a list l as input and returns a new list where each element x is incremented by 1. The script uses a list comprehension to perform this operation, creating the resulting list that's returned. 

This solution is concise and straightforward, showcasing Python's list comprehension feature to efficiently manipulate list elements. 

If you would like to test this script using sample lists, you can run the following commands: 

```python
# Import the incr_list function from the script
from incr_list import incr_list

# Test the incr_list function with example inputs
print(incr_list([1, 2, 3])) # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])) # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```