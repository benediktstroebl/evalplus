```markdown
### Vowels Count Function

#### Problem Description
This function takes a string representing a word as input and returns the number of vowels in the string.
Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

#### Code Implementation

```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it is at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    count = 0
    for i in range(len(s)):
        # Check if the character is a vowel
        if s[i].lower() in vowels:
            # If the character is a vowel, increment the count
            count += 1
        # If the character is 'y' and it's at the end of the string, increment the count
        elif s[i].lower() == 'y' and i == len(s) - 1:
            count += 1
    return count
```

#### Example Use Cases

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello"))  # Output: 2
```

#### Explanation
This function iterates over each character in the input string. If the character is a vowel, it increments the count. If the character is 'y' and it's at the end of the string, it also increments the count. Finally, the function returns the total count of vowels.