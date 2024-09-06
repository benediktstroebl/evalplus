```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

def test_count_distinct_characters(test_str):
    assert count_distinct_characters(test_str) == len(set(test_str))
    return

# Example usage
test_string = 'xyzXYZ jerry foobar'
test_result = count_distinct_characters(test_string)
print(f'Total distinct characters: {test_result}')
```