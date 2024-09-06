```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

string1 = 'XYZ'
string2 = 'jerry'
string3 = 'JER'

if count_distinct_characters(string1) != 3:
    raise ValueError('Wrong result for string1')

if count_distinct_characters(string2) != 4:
    raise ValueError('Wrong result for string2')

if count_distinct_characters(string3) != 4:
    raise ValueError('Wrong result for string3')

if count_distinct_characters(string1) == count_distinct_characters(string2):
    raise ValueError('Ambiguity check failed')

print(count_distinct_characters(string3))
```