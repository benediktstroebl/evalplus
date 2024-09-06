```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using the `split()` method. Then, we iterate through each word, sorting the characters based on their ASCII value and joining them back together into a new word. Finally, we rejoin the new words with spaces to form the `ordered version of the string.` 

The expected output for the test cases provided in the problem statement is:
```
'Hi'
'ehllo'
'Hello !!!Wdlor'
``` 
Which matches the expected output defined in the problem statement.  This solution should pass all the tests and correctly solve the problem.