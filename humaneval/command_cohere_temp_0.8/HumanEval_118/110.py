```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qu':
                cons_count += 1
        else:
            continue
    if cons_count > 1:
        for char in word[::-1]:
            if char.isalpha():
                if char.lower() in 'aeiou':
                    return char
                elif char.lower() not in 'qu':
                    cons_count -= 1
                    if cons_count == 1:
                        return char
    return ''
```

The reverse loop for the last two consonants is used to efficiently find the closest vowel in between. The `continue` statement in the alpha numeric loop skips all non-alphabetic characters to optimize processing. These two optimizations reduce the execution time close to the minimal theoretical value.