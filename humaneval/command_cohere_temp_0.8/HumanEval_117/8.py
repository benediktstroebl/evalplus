Here's a Python script that defines a function `select_words` to solve the problem:
```python
def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = s.split()
    result = [word for word in words if len(word) >= n and sum(1 for char in word if char in consonants) == n]
    return result if result else []
```

The `select_words` function splits the input string into a list of words and then iterates over each word. It counts the number of consonants in each word and compares it to the target number `n`. If a word has exactly `n` consonants, it gets included in the `result` list. Finally, if the `result` list contains at least one word, it's returned; otherwise, an empty list is returned, as per the problem's statement.

The script also includes placeholder tests that can be ran to check if the function `select_words` works correctly. You can run them by adding the following lines at the end of the script:
```python
test_strings = [
    ("Mary had a little lamb", 4, ["little"]),
    ("Mary had a little lamb", 3, ["Mary", "lamb"]),
    ("simple white space", 2, []),
    ("Hello world", 4, ["world"]),
    ("Uncle sam", 3, ["Uncle"])
]

for string, target_consonants, expected in test_strings:
    assert select_words(string, target_consonants) == expected
```

These tests will verify the function against the examples provided in the problem statement.