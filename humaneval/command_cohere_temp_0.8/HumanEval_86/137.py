```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function `anti_shuffle` takes a string as input and returns an ordered version of the string as described in the problem statement. It splits the input string into words separated by spaces. Then, for the first word, it directly joins the characters of the word in sorted order. For each subsequent word, it adds a space before joining the sorted characters. The function then returns the concatenated string of newly ordered words.

Here is an example usage of the function:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will output: "Hello !!!Wdlor", which is an ordered version of the string where each word has been replaced by a new word with all characters arranged in ascending order of their ASCII value. The order of words and blank spaces in the original string is preserved.