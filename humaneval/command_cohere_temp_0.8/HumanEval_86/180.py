```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (using `split()` method on the string), then sorts each word individually based on ASCII values and joins them back to form a new line, and returns the formatted string as the final answer.

Here is a sample output of the function:
```python
anti_shuffle('Hi') returns 'Hi'
anti_shuffle('hello') returns 'ehllo'
anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
```

This can be verified with the following tests:
```python
def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"

test_anti_shuffle()
```

This will run the function's tests and confirm that they pass, proving that the function works correctly and fulfills the requirements of the problem.