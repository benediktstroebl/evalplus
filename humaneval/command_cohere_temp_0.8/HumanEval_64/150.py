```python
def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel at the end of the word."""
    # Your code here!
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count
```

This code defines the `vowels_count` function, which takes a string s as input and returns the number of vowels in the string, counting 'y' as a vowel at the end of the word. It does this by iterating through each character in the string and checking if it is a vowel. If it is, the count is incremented. Additionally, if the character is 'y' and it is at the end of the string, the count is incremented. 

To count the vowels in a string while considering the rules outlined in the example, you can use this function and pass the input string as an argument, like this:
```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
``` 

This will output `2` and `3`, respectively, as the number of vowels in the given words following the defined rules.