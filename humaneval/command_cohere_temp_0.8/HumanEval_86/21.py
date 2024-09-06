```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function first splits the input string `s` into a list of words using the `split()` method. Then, it sorts the characters in the first word ('words[0]') and joins them back together to form a new word. It then does the same for each subsequent word, making sure to insert a space before each new word except for the first one. The resulting string is returned as the ordered version of the input string.

To check the correctness of the solution, let's test it against a few input strings and compare the output with the expected results:
```python
# Test the function with various inputs and compare the output with the expected results
assert anti_shuffle('Hi') == 'Hi'
assert anti_shuffle('hello') == 'ehllo'
assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
```

The test cases above correspond to the problem statement and should help you verify the correctness of the provided solution. You can add more test cases to cover other scenarios if needed.  This solution should effectively handle the task of creating an ordered version of the string while maintaining the order of words and blank spaces.  If you have any more questions or need assistance with anything else, feel free to ask!