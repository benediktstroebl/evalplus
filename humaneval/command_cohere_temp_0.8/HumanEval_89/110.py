```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            encrypted += alphabet[index + 2 * 2:] + alphabet[index:index + 2 * 2]
    return encrypted
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a rotated alphabet technique. It creates an alphabet and shifts each character in the input string by 2 letters, and then by another 2 letters after that, effectively shifting each character down by 4 positions in the alphabet. The function then returns the encrypted string. 

To test the function, you can run the following code: 
```python
TESTS = [('hi', 'lm'), ('asdfghjkl', 'ewhjklnop'), ('gf', 'kj'), ('et', 'ix')]
for test in TESTS:
    assert encrypt(test[0]) == test[1]
```

This tests the example cases provided in the original problem, and can be used to verify the correctness of the encrypted function.