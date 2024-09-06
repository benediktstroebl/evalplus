```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i + 1])] > 1 or letters_count[ord(s[i + 2])] > 1:
            return False
    return True
```

The algorithm works by using a counter for each letter in the alphabet. We increment the counter for the letter if it occurs in the string. Then, for every triple in the string, we check if any of the counters exceed the value of 1. The script returns false if any of these counters are greater than 1. Otherwise, it returns True. 

You can test the function above with test cases like:
```python
test_cases = [
    "abcd", "adb", "xyzabc", "xyzzyx", "aabb", "aabc",
    "aa", "aaaa", "abbb", "english_wordssss"
]

for test in test_cases:
    assert is_happy(test)
``` 

The test cases above include valid and invalid instances of happy strings.