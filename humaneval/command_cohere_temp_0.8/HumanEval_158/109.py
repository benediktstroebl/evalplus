```python
def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for word in words:
        uniq = len(set(word))
        if uniq > max_uniq:
            max_uniq = uniq
            result = word
    return result
```

The function uses a simple algorithm. It first sorts the words list in lexicographical order. Then, it starts iterating through the list, calculating the number of unique characters in each word and keeps the maximum value. As the list is sorted, the first word with the maximum number of unique characters will be the result. 

The `find_max` function can be tested with the following code:
```python
TestFindMax = """
assert find_max(["name", "of", "string"]) == "string", "Simple case failed"
assert find_max(["name", "enam", "game"]) == "enam", "Complex case 1 failed"
assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa", "Complex case 2 failed"
assert find_max(["aaaaaaa", "aaaaa", "aaaa", "aaaaaa"]) == "aaaaaaa", "Edge case failed
"""
```