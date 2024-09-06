```python
def parse_nested_parens(s):
    return [i for i, v in zip(s.split('((()))) if v.startswith('()'), [)]
```

This function splits the string into a list of strings based on the pattern (( )). It then iterates over the list of strings and checks if each string starts with '('. If it does, it adds the corresponding index to the result list.