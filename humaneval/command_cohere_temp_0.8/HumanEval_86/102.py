```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the string `s` and splits it into a list of words using the `split()` method. Then, it iterates through each word in the list, sorts the characters in each word based on their ASCII values, and joins them back together into a new word. It stores these new words in the `new_word_array` list and then joins them together with spaces using the `join()` method to form the final ordered version of the string.

Here is a simple test to verify the function:
```python
def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"

test_anti_shuffle()
```

The test passes with no problems, and the function works as expected.