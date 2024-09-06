```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string, 1)]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("abcd", ["ab", "bc", "cd"]),
    ("123", ["1", "12", "123"]),
    ("", []),
    ("#", ["#"])
]

def test(test_case):
    actual = all_prefixes(test_case[0])
    assert actual == test_case[1]

test_suite = [test_case for test_case in test_cases]

test_results = {}
for test_case, expected in test_suite:
    test(test_case)
    test_results[test_case] = True
print(test_results)
 ```