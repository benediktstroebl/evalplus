```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.cloud() if c.isalpha()})

def test_distinct_characters() -> None:
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("JERRY") == 4
    assert count_distinct_characters(" !") == 4
    assert count_distinct_characters(" Jerry ") == 4
    assert count_distinct_characters("   jerryX ") == 4
    assert count_distinct_characters("   jerry   ") == 4
    assert count_distinct_characters(" .^* $") == 4
    assert count_distinct_characters("	") == 5  # Extra whitespace should count distinct characters
    assert count_distinct_characters("abc") == 3  # Lowercase letters count as distinct characters
    assert count_distinct_characters(" Judge ") == 3  # Dashes and capital letters
```