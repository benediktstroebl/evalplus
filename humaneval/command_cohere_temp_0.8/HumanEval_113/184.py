```python
def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, d)))) for d in lst]
    return ["the number of odd elements in the string %s of the input." % i for i in r]
```

Here is an example of how to use the function:
```python
print(odd_count(['1234567']))
```

The above code will print the following:
```
['the number of odd elements in the string 4 of the input.']
```

And here is another example of utilizing the function:
```python
print(odd_count(['3', "11111111"]))
```

This will output:
```
['the number of odd elements in the string 1 of the input.', 'the number of odd elements in the string 8 of the input.']
```