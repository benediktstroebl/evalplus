```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The anti_shuffle function splits the input string into a list of words, and then joins each word in the list, sorting the characters according to their ASCII values. This process is repeated for each word in the list, with a space added between them to ensure the word order is preserved. The resulting string is returned as the ordered version. 

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will output the ordered version of the string "Hello World!!!", where the characters are sorted according to their ASCII values, and the words are separated by spaces.