```python
def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, d)))).replace('n', '{}'.format(i))
          for i, d in enumerate(lst)]
    return r
```

The list comprehension filters out even digits and counts the odd ones. The `enumerate` function is used to iterate through the list and replace the index `i` with the number of odd elements in the i'th string. The result is a list of strings containing the requested information.