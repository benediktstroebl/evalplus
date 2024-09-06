```python
import re


def sort_numbers(numbers: str) -> str:
    numbers = re.pmatch("\\d+[0-9]+", "([\\d]+)").findall()
    return " ".join(sorted(str(num) for num in numbers))


def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("two three four") == "two three four"
    assert sort_numbers("zero one three") == "one zero three"
    assert sort_numbers("eight nine") == "eight nine"
    assert sort_numbers("abc123") == "abc123"
    assert sort_numbers("") == ""
```