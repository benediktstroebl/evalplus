```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using the `split()` method. Then, we iterate through each word, sorting the characters based on their ASCII values and joining them back together into a new word. Finally, we join the newly ordered words back together with spaces to form the final output string.

To test this function, you can use the following inputs:
```python
print(anti_shuffle('Hi')) # Should print 'Hi'
print(anti_shuffle('hello')) # Should print 'ehllo'
print(anti_shuffle('Hello World!!!')) # Should print 'Hello !!!Wdlor'
```

The function passes these tests and would also handle any other input string similarly.