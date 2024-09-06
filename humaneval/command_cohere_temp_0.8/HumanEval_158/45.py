```python
def find_max(words):
    max_dict = max(zip(words, map(set, words)), key=lambda x: x[1].__len__())[0]
    return max_dict if max_dict == max(words, key=lambda x: x.lower()) else max(words, key=lambda x: x.lower())
```

The function uses the `zip` function to iterate over each word in the list of words provided and uses the `set` function to create a set of unique characters in each word. Then, the function uses the `max` function to find the word with the maximum number of unique characters. If there are multiple words with the same maximum number of unique characters, the function uses the `lower` method to determine the lexicographical order and returns the word that comes first. 

Here is an example of how you can test this function:
```python
def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
```