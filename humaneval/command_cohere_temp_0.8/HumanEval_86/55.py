Here's a Python script that contains a function called anti_shuffle, defined as follows:
```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```
This anti_shuffle function takes a string s as input and returns an ordered version of the string, where all the words are replaced by a new word with all the characters arranged in ascending order based on their ASCII value. The function first splits the input string s into a list of words using the split() method. Then, it creates a new word by joining the characters of the first word in ascending order using the sorted() function. Subsequently, it iterates through the remaining words in the list, appending a space followed by the sorted version of each word to the new_word. Finally, the function returns the formatted new_word as the ordered version of the input string.

Here's an example usage of(+the above function+):
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

And here's another example to illustrate different input cases:
```python
print(anti_shuffle("hi")) # output: "hi"
print(anti_shuffle("hello")) # output: "ehllo"
``` 
This will produce the following results:
```
hello !!!Wdlor
hi
ehllo
```