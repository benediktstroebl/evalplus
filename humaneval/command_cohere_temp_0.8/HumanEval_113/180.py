```python
def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, num))))
         for num in lst]
    return ['the number of odd elements ' + str(i) + 'n the string ' + str(i) + ' of the input.'
            for i in range(len(r))]
```