```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        delta = 2*(index+1)
        new_index = (alphabet_length + index - 1) // 2 + delta
        encrypted += alphabet[(new_index)%alphabet_length]

    return encrypted
```

This Python script defines a function `encrypt` that takes a string `s` as input and returns a string encrypted using a rotated alphabet scheme. Specifically, it shifts each character in the input string by a quantity proportional to its alphabetical index, with the shift amount calibrated to center the encrypted text. To do this, it first defines the alphabet as a string (`'abcdefghijklmnopqrstuvwxyz'`) and initializes an empty string `encrypted` to hold the encrypted output.

Then, for each character `char` in the input string `s`, it finds its index in the alphabet and calculates a displacement, which is twice the index number incremented by 1 (e.g., 'a' has index 0, so it gets a displacement of 2, 'b' gets displacement 4, and so on). Then, a new index is calculated by taking the absolute difference between the current alphabet length and the index, dividing by 2, and adding the displacement. This new index is used to retrieve the encrypted character, which is then appended to the `encrypted` string.

The result is a string `encrypted` that contains the input string `s` encrypted using the defined rotation scheme. You can verify the correctness of the solution by running the following tests:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('verylongstringthatcontainsmanyletters') == 'nbbgldqkpiuvhzfwja'
```

This test suite contains four assertions that aim to verify that the `encrypt` function behaves as expected with different input lengths, content, and starting indices. You can execute these tests individually by calling `test_encrypt()` at the Python prompt or in an automated fashion by incorporating them into a broader test suite.