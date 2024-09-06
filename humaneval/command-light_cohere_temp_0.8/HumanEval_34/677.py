```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, float('inf')] + seen]

#Test cases
tests = {
    'input': [5, 3, 5, 2, 3, 3, 9, 0, 123],
    'expected': [0, 2, 3, 5, 9, 123]
})

result = unique(tests['input'])

print(f'The output is: {result}')
```