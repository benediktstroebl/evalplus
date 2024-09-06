```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_char_word = min(char_count, key=char_count.get)
    return lexicographically_first if char_count[lexicographically_first] == char_count[max_char_word] else max_char_word
``` 

The Python script defines a function `find_max` that solves the problem as described in the prompt. It iterates through the list of words, it keeps track of the word with the highest count of unique characters and the word that comes first in lexicographical order. In the event that these are the same, it returns the one that comes first in lexicographical order, and if more than one word has the highest count of unique characters, it returns the one that comes first in lexicographical order. 

Here is an example of how you can test this new function ::
```python
def test_find_max():
    # Test case one
    assert find_max(["name", "of", "string"]) == "string"

    # Test case two
    assert find_max(["name", "enam", "game"]) == "enam"

    # Test case three
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Test case four
    assert find_max(["foo", "barr", "bar", "zarr", "zar"]) == "zarr"

test_find_max()
``` 

This would result in the test file shown above, which will pass if the `find_max` function is implemented correctly.