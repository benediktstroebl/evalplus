```python
def find_max(words):
    char_count = {}
    max_char_word = None
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if max_char_word is None or char_count[word] > char_count[max_char_word]:
            max_char_word = word
    return max_char_word
```

The function employs a dictionary named `char_count` to record the count of unique characters in each word. After iterating through the list of words, it compares the character count of each word with the current maximum (`max_char_word`) and updates it if a higher count is found. Finally, it returns the word with the maximum number of unique characters.

The following is a test script that can be used to validate the function:
```python
def test_find_max():
    # Test Case 1
    assert find_max(["name", "of", "string"]) == "string"

    # Test Case 2
    assert find_max(["name", "enam", "game"]) == "enam"

    # Test Case 3
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Test Case 4
    assert find_max(["hello", "world", "hello"]) == "hello"

test_find_max()
```

This test script contains four test cases, and each one verifies a specific scenario to ensure the correctness of the `find_max` function.