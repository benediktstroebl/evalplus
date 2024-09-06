```python
def odd_count(lst):
    r = [str(len(re.findall(r'1|3|5|7|9', s)))
          for s in lst]
    return ['the number of odd elements ' + ''.join(x) + 'n the str' + ''.join(y) + 'ng ' + ''.join(z) + ' of the ' + ''.join(u) + 'nput.'
            for x, y, z, u in zip(r, r, r, lst)]
```