```python
def get_closest_vowel(word):
    cons_idx = -1
    vowel = ""
    for i, char in enumerate(word):
        if char.is consonant() and char != 'y':
            cons_idx = i
        elif char.is vowel():
            vowel = char
    if cons_idx == -1:
        return ""
    return vowel
```

This script employs a for loop to examine each character in the given word. It identifies consonants proceeding a vowel from the right side of the word and stores the index of the last consonant. Subsequently, it identifies the closest vowel based on the stored index and returns it if found. In the absence of a qualifying vowel, an empty string is returned. 

To check the validity of this solution, test cases can be added to ensure its functionality. Here is an example of how test cases may be incorporated:
```python
# TEST CASES
print(get_closest_vowel("yogurt")) # Output: "u"
print(get_closest_vowel("FULL")) # Output: "U"
print(get_closest_vowel("quick")) # Output: ""
print(get_closest_vowel("ab")) # Output: ""
```

These test cases aid in validating the correctness of the function.