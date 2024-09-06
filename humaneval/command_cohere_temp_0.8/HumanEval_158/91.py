```python
def find_max(words):
    words.sort()
    max_set = set()
    for word in words:
        char_set = set(word)
        if len(char_set) > len(max_set):
            max_set = char_set
    for word in words:
        if set(word) == max_set:
            return word
    return words[0]
```

The function first sorts the list of words lexicographically. It then uses an outer loop to iterate through the words and an inner loop to iterate through the characters of each word, creating a set of unique characters for each word. This allows it to maintain a maximum set of unique characters seen so far, which corresponds to the word with the most unique characters.

We can update the markdown code block to include some tests for the function:
```python
```python
def test_find_max():
    # basic tests
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # edge cases
    assert find_max(["a", "b", "c", "a", "b"]) == "a"
    assert find_max(["a", "b", "c", "d", "e", "a"]) == "a"
    assert find_max([]) == None

    # case when multiple words have maximum length
    assert find_max(["abcd", "efgh", "ijkl", "abcf"]) == "abcd"
```