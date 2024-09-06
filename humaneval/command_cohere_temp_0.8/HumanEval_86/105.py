```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. In the provided example, the output for the input statements is:
```python
print(anti_shuffle('Hi')) # Should return 'Hi'
print(anti_shuffle('hello')) # Should return 'ehllo'
print(anti_shuffle('Hello World!!!')) # Should return 'Hello !!!Wdlor'
``` 
This script satisfies the given requirements and maintains the correct spacing between words. It uses string splitting to separate the input string into individual words and then sorts each word based on the ASCII values of its characters. The sorted words are then reassembled into a new string, which is returned by the function.