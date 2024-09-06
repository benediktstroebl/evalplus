```python
def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
    
def select_words(s, n):
    """
    Selects words from a string that contain exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is used to count the number of consonants in a given word. All computations on the string are done in lower case to make the problem less case-sensitive. The `select_words` function takes a string and a number n as input and returns a list of all words that contain exactly 'n' consonants, in order these words appear in the string. 

Here is an example usage of the function for the input "Mary had a little lamb", 4:
```python
select_words("Mary had a little lamb", 4)
```
Which returns the output: ```python
["little"]
``` 

Here is an example usage of the function for the input "Hello world", 4:
```python
select_words("Hello world", 4)
```
Which returns the output: ```python
["world"]
``` 

And here is an example usage of the function for the input "Uncle sam", 3:
```python
select_words("Uncle sam", 3)
```
Which returns the output: ```python
["Uncle"]
```