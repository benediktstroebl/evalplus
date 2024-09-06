```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.set_split(string) for _ in string.prefix_list()]
```

def string_is_prefix(string: str, prefix: str) -> bool:
    return string.startswith(prefix)

def test_prefixes() -> None:
    test_cases = [
        ("mype", "mype"),
        ("work", "work"),
        ("abc", "ab"),
        ("hello world!", "hello"),
        ("", " ")
    ]
    for text, expected_prefixes in test_cases:
        for expected in expected_prefixes:
            if not_is_prefix(text, expected):
                print(f"Error: {text} should have prefix {expected}, but didn't.")
                break
        print(f"Correct: {text} has prefix {expected}")
    return None
```