```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This function defines vowels and then loops through the input string character by character, checking if each character is uppercase and a vowel. If it is, it increments the count, and afterward, returns the total count. This should correctly solve the problem for relevant test cases. Let me know if you'd like to test other cases or explain any other approaches to solve this!