```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char == string[-1]:
            count += 1
        else:
            break
    return count

# Test the function
test_cases = [
    ("", "a"),
    ("aaa", "aa"),
    ("aaaa", "aa"),
    ("puts artificial text here", "a")
]

for text, sub in test_cases:
    result = how_many_times(text, sub)
    print(f"{text}:{sub} => {result}")
```  This code defines a function that finds the frequency of a given substring in a given string, and tests this function with various inputs.