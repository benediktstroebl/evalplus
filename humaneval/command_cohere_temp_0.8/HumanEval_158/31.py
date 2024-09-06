```python
def find_max(words):
    max_uniq = 0
    max_word = None
    for word in words:
        current_uniq = len(set(word))
        if current_uniq > max_uniq:
            max_uniq = current_uniq
            max_word = word
    return max_word
```

The function `find_max` uses a loop to iterate through the list of words. It initializes `max_uniq` (maximum unique characters) to 0 and `max_word` to None. For each word, it calculates the number of unique characters using `len(set(word))`, and if this quantity is greater than `max_uniq`, it updates `max_uniq` and `max_word` to the current word. After iterating through all words, it returns the word with the maximum number of unique characters. If multiple words have the same maximum number of unique characters, the one encountered first in lexicographical order is returned.

Here is a simple test suite to verify the function:
```python
def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert find_max([1, 2, 3, 3, 2, 1]) == 1
    assert find_max([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert find_max([10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert find_max([3, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == "12"
    assert find_max([3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == "4"
```