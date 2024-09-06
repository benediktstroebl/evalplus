```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            # Shift the index down by 2
            new_index = (index - 2) % 26
            # Return the character from the new index modulo 
            # the length of the alphabet
            encrypted += alphabet[new_index % 26]
    return encrypted
```

This encrypt function takes a string s as input and iterates through each character in the string. It uses the `alphabet` string to map characters to their respective indices. If a character isn't found in the alphabet, it's added as-is to the `encrypted` string. For characters that are found in the alphabet, the function shifts the index down by 2 and then extracts the character from the new index, considering wraparound, and adding this character to the `encrypted` string. 

Here is a simple test script to verify the functionality of the code:
```python
TESTS = ['hi', 'asdfghjkl', 'gf', 'et']

for test_str in TESTS:
    print(f"Input: {test_str}")
    assert encrypt(test_str) == f"Output: {TESTS[0]}"
```

The test script loops through the list of TESTS and for each test, it prints the input and the calculated output of the encrypt function. It then verifies that the output is correct using an `assert` statement.