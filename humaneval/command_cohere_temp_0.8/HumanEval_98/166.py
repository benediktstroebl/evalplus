```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to check
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count
```

This script defines a function `count_upper()` which takes a string `s` as an input and returns the number of uppercase vowels in even indices of that string. The function initially constructs a string consisting of all the uppercase vowels to check, namely 'AEIOU'. It then sets the count to 0 to prepare to tally the vowels. The function subsequently iterates through the input string `s` by stepping twice at a time (range(0, len(s), 2)), checking each character in even indices to determine if it is an uppercase vowel, and incrementing the count if it is. The function finally returns the total count of uppercase vowels in even indices. 

The expected time complexity of the script is O(n/2), where n is the length of the input string, and the space complexity is O(1) as it only uses a constant amount of memory to store the input string and the variable to count the number of uppercase vowels. 

To verify the correctness of the script, three tests could be conducted:
1. Testing a string with all uppercase vowels in even indices: `count_upper('AAAAAAA')` should return a count of 6. 
2. Testing a string with all lowercase vowels in even indices: `count_upper('aaaaaaa')` should return a count of 0. 
3. Testing a string with mixed case and no vowels in even indices: `count_upper('BbBbCcCcDdD')` should return a count of 0. G 

These tests would confirm that the function is correctly counting only the uppercase vowels in even indices and ignoring vowels in other cases or in odd indices.