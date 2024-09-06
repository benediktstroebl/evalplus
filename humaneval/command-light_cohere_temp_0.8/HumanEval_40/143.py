```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in zip(*l)))

#Test cases
tests = [
     {'input': [1, 3, 5, 0],
      'output': False,
      'type': 'bool'}
     ,{' input': [1, 3, -2, 1],
       'output': True,
       'type': 'bool'}
     ,{' input': [1, 2, 3, 7],
       'output': False,
       'type': 'bool'}
     ,{' input': [2, 4, -5, 3, 9, 7],
       'output': True,
       'type': 'bool'}
     ,{' input': [],
       'output': False,
       'type': 'bool'}

# Function call
triples_sum_to_zero = triples_sum_to_zero

#Test cases
for k, v in tests.
```