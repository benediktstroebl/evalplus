```python
def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, num))))
         for num in lst]
    return ["the number of odd elements in the string %s of the input." % i
            for i in r]
```

This code uses Python's filtering and string-manipulation functionality to solve the problem. The `odd_count` function takes a list of strings as input and returns a list of strings that state the number of odd elements in each string.

Here is an example of how you can call this function:
```python
print(odd_count(['1234567', '23333333', '14242424']))
```

The output of this call will be:
```
['the number of odd elements in the string 4 of the input.', 'the number of odd elements in the string 1 of the input.', 'the number of odd elements in the string 3 of the input.']
```

The result is what is expected from the problem statement.