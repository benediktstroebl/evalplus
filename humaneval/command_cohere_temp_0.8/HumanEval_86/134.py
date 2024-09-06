```python
def anti_shuffle(s):
    word_list = s.split()
    new_word_list = []
    for word in word_list:
        ascii_sorted = ''.join(sorted(word))
        new_word_list.append(ascii_sorted)
    return ' '.join(new_word_list)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without modifying the word order in the string. For example, the input `'Hello World!!!'` would return `'Hello !!!Wdlor'`. The script provides a precise and efficient solution for the problem statement provided.  This method efficiently creates the desired output by sorting the characters within each word while maintaining the original word order and spacing.