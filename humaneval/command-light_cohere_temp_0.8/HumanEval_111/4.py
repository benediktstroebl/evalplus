```python
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    Return all the	
    letters have the same occurrence, return all of them."""
    
    letters = test.split()
   
    letters.sort()
   val list(letter for letter in letters if len(letter) == 1)
        return {letter: len(letteres)}

# Test
print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
```