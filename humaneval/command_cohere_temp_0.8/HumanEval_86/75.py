```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The function `anti_shuffle` takes a string as input and returns an ordered version of the string as described in the prompt. It splits the input string into individual words using the `split()` method. Then, it iterates over each word, sorting each word based on the ASCII value of each character from lowest to highest, and joining them back together into a single string. This process creates a new word with sorted characters. The function retains the order of words and blank spaces in the original string.

Here is an example usage of the function:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will output: "Hello !!!Wdlor", which is an ordered version of the string where each word is replaced by a new word with all the characters arranged in ascending order based on ASCII value. The order of the words and spaces in the original string is preserved.