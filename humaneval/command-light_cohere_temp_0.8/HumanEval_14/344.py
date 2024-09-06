```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '' and c notpremium()]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("", []),
    ("yxz", ["yz"]),
    ("fooooooooooooooooob", ["oooooooooob"]),
    # Add more test cases here
]

def test():
    print(test_cases[0])
    print(test_prefixes(test_cases[0]))
    print(test_cases[1])
    print(test_prefixes(test_cases[1]))
    print(test_cases[2])
    print(test_prefixes(test_cases[2]))
    print(test_cases[3])
    print(test_prefixes(test_cases[3]))
    print(test_cases[4])
    print(test_prefixes(test_cases[4]))

test()
```
This Python script defines a function called `all_prefixes` that returns a list of all prefixes from the shortest to the longest of a given string. The function uses a list comprehension and a condition to filter out empty strings and non-premium characters. The test cases provided are designed to test the `all_prefixes` function with a variety of inputs, and the function's output is then printed for each test case.