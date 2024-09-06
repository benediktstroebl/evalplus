```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. In the provided example, the output for the input sentences is:
```python
print(anti_shuffle('Hi')) # Should print 'Hi'
print(anti_shuffle('hello')) # Should print 'ehllo'
print(anti_shuffle('Hello World!!!')) # Should print 'Hello !!!Wdlor'
``` 
This script will provide the correct output for the given input sentences.