```markdown
### Vowels Count Function
#### Problem Description
Write a function `vowels_count` which takes a string representing a word as input and returns the number of vowels in the string. 
Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

#### Solution
```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Define the vowels
    vowels = 'aeiou'
    
    # Check if the string is not empty
    if not s:
        return 0
    
    # Check if the last character is 'y'
    if s[-1].lower() == 'y':
        # Add 'y' to the vowels string
        vowels += 'y'
    
    # Count the vowels
    count = sum(1 for char in s.lower() if char in vowels)
    
    return count
```

#### Example Usage
```python
print(vowels_count("abcde"))  # Outputs: 2
print(vowels_count("ACEDY"))  # Outputs: 3
print(vowels_count("hello"))  # Outputs: 2
print(vowels_count("aeiou"))  # Outputs: 5
print(vowels_count("bcdfg"))  # Outputs: 0
```

#### Note
This function uses a generator expression to iterate over each character in the string and count the number of vowels. It also checks if the last character of the string is 'y' and adds it to the vowels string if it is. The function returns the count of vowels in the string.