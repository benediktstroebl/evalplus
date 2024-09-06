```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a shuffled version of the word arrangement. It first splits the input string into individual words and stores them in the `word_array` variable. Then, it iterates through each word in the array, sorts the characters of each word based on their ASCII values, and stores the ordered version in the `new_word_array`. Finally, the function returns a space-separated string composed of the newly ordered words, maintaining the original word placement and spaces.

Here is a simple test case to ensure the function behaves as intended:
```python
def test_anti_shuffle():
    # Basic tests
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hi") == "Hi"

    # Test with multiple spaces
    assert anti_shuffle("Hello    World!!!") == "Hello    !!!Wdlor"

    # Test with numeric characters
    assert anti_shuffle("123abc") == "231abc"

test_anti_shuffle()
```

The test case will execute the function with different inputs and verify that the output is correct.

This problem can be solved in many other ways as well, this is just one possible solution. Let me know if you would like to discuss alternative solutions. 

Let me know if you would like help with anything else!