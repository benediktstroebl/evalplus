```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This script takes a string and returns a new string where every word has been replaced with a new word consisting of the same characters, ordered alphabetically by their ASCII values. The order of words and spaces is preserved.

The given examples would yield the following results:
- `anti_shuffle('Hi') returns 'Hi'` 
```python
>>> anti_shuffle('Hi')
'Hi'
```

- `anti_shuffle('hello') returns 'ehllo'`
```python
>>> anti_shuffle('hello')
'ehllo'
```

- `anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'`
```python
>>> anti_shuffle('Hello World!!!')
'Hello !!!Wdlor'
```