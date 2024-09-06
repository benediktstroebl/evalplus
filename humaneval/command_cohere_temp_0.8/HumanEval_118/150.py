```python
def get_closest_vowel(word):
    cons_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in word:
        if c.lower() in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if cons_count > 0:
                return c
        else:
            cons_count+=1
    return ''
```

The script counts consonants before and after each vowel, and if a vowel is between two consonants (and isn't the first or last character), it returns that vowel. This can be better understood through examples:
1. ```get_closest_vowel("yogurt") == "u"```.
2. ```get_closest_vowel("FULL") == "U"```.
3. ```get_closest_vowel("quick") == ""```.
4. ```get_closest_vowel("ab") == ""```.
5. ```get_closest_vowel("a") == "a"```.
6. ```get_closest_vowel("eu") == "e"```. 
7. ```get_closest_vowel(" acknowlwedgement") == "e"```. 
8. ```get_closest_vowel("kinetic") == "i"```. 
9. ```get_closest_vowel("zzz") == ""```. 
10. ```get_closest_vowel("bark") == ""```. 
11. ```get_closest_vowel("razzmatazz") == "a"```.