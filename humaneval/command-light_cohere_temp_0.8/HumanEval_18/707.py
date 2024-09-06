```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Return count of occurrences of substring in string, without overlapping.
    """ 
    return sum(1 for i, x in enumerate(string.find(substring): 
                            1 if x == substring else 0) 
)

def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3

print("tests passed!")
```