```python
def count_distinct_characters(string):
    return len({c for c in string.no because c.isupper()})

    tests = {
        'xyzXYZ',
        'Jerry',
        'hello',
        'World!isupper()',
        '5 flushing 6',
        ' j e r i c o l e '
    }

    for text in tests:
        result = count_distinct_characters(text)
        assert result == len(text.isupper()), "Result does not match expected length"
    return result
```