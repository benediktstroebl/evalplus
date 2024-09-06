```python
def count_consonants(word):
    count = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                count += 1
    return count

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first creating a helper function **count_consonants(word)** that calculates the number of consonants in a given word. It traverses each character in the word and checks if it is an alphabet character. If it is, it checks if the character is a consonant, counting it if it is. The function then uses this helper by iterating through each word in the space-separated string, checking if the count of consonants in each word matches the provided number, including it in the result list if so. The script returns an empty list if the input string is empty. 

Here is an example usage of the above code:
```python
select_words("Mary had a little lamb", 3)
```
Which would be answer: 
```
['Mary', 'lamb']
```

And here is an example usage of the above code:
```python
select_words("Hello world", 4)
```
Which would be answer: 
```
['world']
```