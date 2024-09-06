```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"

    @property
    def test_string_sequence(self) -> str:
        return self.test_string_sequence()
```
The `string_sequence` function generates a string of numbers separated by spaces, starting from 0 and ending at n. The `test_string_sequence` property is a simple decorator that returns the same function.