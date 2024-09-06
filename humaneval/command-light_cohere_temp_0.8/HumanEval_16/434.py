```python
def count_distinct_characters(string: str):
    return len({c for c in string.string() if c.isalpha()})
 string. how to be a distinct character
    ```
def test_distinct_characters():
    assert count_distinct_characters('xyXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```