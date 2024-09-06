```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"
   
    # tests
    assert len(string_sequence(5)) == 7
    assert string_sequence(0) == '0'
    assert string_sequence(10) == '10000'
```