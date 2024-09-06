```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) ^ 1, txt.lower())))
    return ans
```

The provided Python script solves the problem by performing the following steps:
1. Check if the string contains a comma (`,`) by using the `in` operator, if found, it means there are no spaces or odd letters, so it splits the string into a list using the `split()` method, where the delimiter is a comma.
2. If the above condition is not met, the script checks if the string contains any whitespace characters (space) using the `in` operator again. If found, it means there are no commas or odd letters, and it splits the string into a list using the `split()` method, where the delimiter is a space.
3. If both conditions are not met, it means there are no commas or spaces, and the string must be a non-empty string of characters with odd ASCII values. The script filters the characters from the string, using a generator expression with a filtering function in a list comprehension, where `lambda c: ord(c) ^ 1` checks if the ASCII value of the character is odd, and `filter(..., txt.lower())` converts all characters to lowercase to make the check case insensitive. The `len()` method returns the length of the filtered list.

The script returns the appropriate answer based on the conditions checked in the provided string.