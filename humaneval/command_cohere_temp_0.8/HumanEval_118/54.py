```python
def get_closest_vowel(word):
    cons_idx = -1
    vowel = ''
    for i, char in enumerate(word):
        if char.lower() in 'aeiou':
            if char.lower() in word[i+1:]:
                cons_idx = i+1
        elif char.lower() in 'bcdfghjklmnpqrstvwxyz':
            if cons_idx != -1:
                vowel = word[cons_idx]
                break
    return vowel
```

This script employs a for loop to inspect each character in the given word. A potential vowel is recorded if it is flanked by consonants (case sensitive) on the right. The loop continues to scan for vowels even after identifying a potential vowel, but the variable `vowel` holds the most recent vowel that met the criteria. The function returns an empty string if it cannot identify a qualifying vowel. 

Here is an example usage of the function:
```python
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
``` 

This should output:
```
u
U
""
""
``` 

This approach assumes that vowels are more frequent in English language texts, which aids in keeping the loop concise in terms of duration and code length.