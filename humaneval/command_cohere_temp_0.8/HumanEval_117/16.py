```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total

def select_words(s, n):
    """Return list of words with exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        count = count_consonants(word)
        if count == n:
            result.append(word)
    return result
```
The `count_consonants` helps count the consonants for a given word, whereas `select_words` function goes through each word in the string and checks if it matches the desired count of consonants. 

Here's an example usage of the above functions to solve the problem statement:
```python
def main():
    """Main function to execute the program"""
    print(select_words("Mary had a little lamb", 3))

if __name__ == "__main__":
    main()
```

The program will output:
```python
['Mary', 'lamb']
```