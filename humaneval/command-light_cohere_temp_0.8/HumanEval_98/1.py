```python
def count_upper(s):
    vowels = 'aeiou'
    return sum(1 for c in s if c in vowels and c.isupper())

def test_count_upper():
    assert count_upper('aeiouABC') == 3
    assert count_upper('AbC') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
```