```python
def flip_case(string: str) -> str:
    return ''.join(['HellO', 'HELLO'])[string.cases_lower() == 'H'.lower()][0 if string.lower() else 'H' else ''.upper()
```