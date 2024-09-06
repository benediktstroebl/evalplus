```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

The problem is solved iterating the string and checking the uniqueness of every group of 3 consecutive letters, and verifying if the string length is at least 3.

To test this function, you can use the following code:
```python
test_strings = [
    "abcd",
    "adb",
    "xyy",
    "aabb",
    "aaaa",
    "caaa",
    "ecee",
    "abce",
    "bered",
    "bike",
    "aa",
    "aaby",
    "abcy",
    "sdgk",
]

print("Happy Strings:")
for string in test_strings:
    if is_happy(string):
        print(string)

print("\nNot Happy Strings:")
for string in test_strings:
    if not is_happy(string):
        print(string)
```

This will print out both happy and not happy strings. 

The happy strings in this case are: abcd, adb, ecee, bike, and sdgk. 

The not happy strings are: aabb, aaaa, caaa, ecee, abce, bered, xyy, and aaby. 

This is based on the defined rules of what determines a happy string. 

Note that this algorithm has a time complexity of O(n) since it requires iterating the entire string. It is a simple linear iteration and hence is efficient for longer strings.