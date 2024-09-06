```python
def odd_count(lst):
    r = [str(len(re.findall(r'o{2,}', s))) for s in lst]
    return ['the number of odd elements ' + ''.join(map(str, i)) + ' in the string ' + ''.join(map(str, j)) + ' of the input' for i, j in zip(r, lst)]
```