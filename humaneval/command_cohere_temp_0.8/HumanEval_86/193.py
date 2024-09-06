Here's a Python script that contains a function called anti_shuffle, defined to solve the problem as described:
```python
def anti_shuffle(s):
    word_starts = [i for i, char in enumerate(s) if char != ' ' and i == len(s) - len(char)]
    sorted_words = [char for char in s if char != ' ' and char]
    sorted_words = sorted(sorted_words, key=str.lower)
    return ' '.join([s[:word_starts[i]] + sorted_words[i:] for i in range(len(sorted_words))])
```

This function uses list comprehensions to find the starting indices of each word (where the word starts and the previous element is a space), sorts the words based on their lowercase representation, and then rebuilds the string by maintaining the original spacing and inserting the sorted words correctly.

The code includes tests that cover several edge cases:
```python
def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("   ") == "   "
    assert anti_shuffle("aA") == "aA"
    assert anti_shuffle("zZ") == "zZ"
    assert anti_shuffle("Zone!") == "Zoen!!"
    assert anti_shuffle("Example String With Numbers 1-9") == "Example String With Numbers 1-9"
```