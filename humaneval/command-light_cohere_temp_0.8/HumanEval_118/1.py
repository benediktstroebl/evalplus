```python
def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    for c in word[1:]:
        if c in vowels:
            return c
    return ""

# Test
test_case = ["ab","dolor","quick","full","hello"]
for t in test_case:
    got = get_closest_vowel(t)
    assert got == t[0]
```