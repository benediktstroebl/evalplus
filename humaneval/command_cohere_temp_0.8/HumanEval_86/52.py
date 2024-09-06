```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```

The `anti_shuffle` function takes a string as input and returns an ordered version of the string as described in the problem statement.

The above approach divides the given string into a list of words using the `split()` method. Then, it sorts the characters of the first word (or any word) in ascending order to create a new word. After that, it iterates through the remaining words and creates a new word by sorting their characters. The process continues until all the words are processed. Finally, the new word is returned which contains all the words of the original string sorted in ascending order. 

Note, this solution assumes that words in the input string are separated by spaces, and the order of words and spaces between them should be preserved in the output. If the input may contain different types of whitespace or special characters between words, extra processing may be necessary to correctly extract the words and maintain the desired order.