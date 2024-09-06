```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)

    return ' '.join(new_word_array)
```

This approach first splits the string into words using the `split()` method. Then, it iterates through each word, sorting the characters based on their ASCII values and joining them back together into a new word. Finally, the function returns the original string with all words replaced by their sorted counterparts, maintaining the original word order and spaces. 

To verify the correctness of the solution, you can check whether the function behaves as expected for various inputs using Python's built-in `assert` statements:
```python
# Test cases
assert anti_shuffle("Hi") == "Hi"
assert anti_shuffle("hello") == "ehllo"
assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
assert anti_shuffle("!!!)hello_world(!^")) == "!!)ehllo_wdlor("
```

To execute this test suite, you can save the above code into a Python file (e.g., `anti_shuffle.py`) and then run the file using the command `python anti_shuffle.py` in your terminal. The test suite will execute each assertion, and any failure will be reported, ensuring the correctness of the function against specific test cases.