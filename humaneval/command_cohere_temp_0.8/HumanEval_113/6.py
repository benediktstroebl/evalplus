```python
def odd_count(strings):
    lst = [str(len(list(filter(lambda d: d % 2 == 1, s))) )
           for s in strings]
    lst = ['the number of odd elements ' + i + ' in the string ' + i + ' of the input.'
            for i in lst]
    return lst
```

This script defines a function `odd_count` takes a list of strings as input and returns a list where each element is a string containing the count of odd digits in the corresponding string from the input. The `filter` function is used with a lambda to filter out even digits. The resulting list of filtered digits is counted using the `len` function, and then a string manipulation is performed to achieve the required return list formatting.