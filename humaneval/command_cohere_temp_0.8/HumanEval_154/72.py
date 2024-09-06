```python
def cycpattern_check(a, b):
    a, b = a.lower(), b.lower()
    return any(b in rotated_string for rotated_string in (a[i:]+a[:i]) if i!=len(a))
```
This function takes two string inputs and rotates the second string through all permutations. It then checks if any of the permutations match a substring in the first string. The function returns True if a match is found and False otherwise. 

Here is a unit test that can be used to validate the functionality of the function:
```python
def test_cycpattern_check():
    # Test string 1: Cycle through lowercase letters
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("abcd","bad") == True
    assert cycpattern_check("abcd","bda") == True
    assert cycpattern_check("abcd","dab") == True

    # Test string 2: Cycle through uppercase letters
    assert cycpattern_check("HELLO","ELL") == True
    assert cycpattern_check("HELLO","LEL") == True
    assert cycpattern_check("HELLO","LLE") == True
    assert cycpattern_check("HELLO","LOE") == True

    # Test string 3: Cycle through mixed case letters and numbers
    assert cycpattern_check("Whassup","Psus") == False
    assert cycpattern_check("Whassup","suP") == True
    assert cycpattern_check("Whassup","sUp") == True
    assert cycpattern_check("Whassup","UpS") == True

    # Test string 4: Cycle through same strings
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("abab","abba") == True
    assert cycpattern_check("abab","baab") == True
    assert cycpattern_check("abab","baba") == True

    # Test string 5: Different strings
    assert cycpattern_check("efef","eeff") == False

    # Test string 6: Cycle through punctuations
    assert cycpattern_check("himenss","simen") == True
    assert cycpattern_check("himenss","mensi") == True
    assert cycpattern_check("himenss","menji") == True
    assert cycpattern_check("himenss",".msni") == True
    assert cycpattern_check("himenss",".imens") == True

    # Test string 7: Cycle through different punctuations
    assert cycpattern_check("(!@#$%^&*()","()") == True
    assert cycpattern_check("(!@#$%^&*()",".()") == True
    assert cycpattern_check("(!@#$%^&*()",")(*)") == True
    assert cycpattern_check("(!@#$%^&*()","(*") == True
    assert cycpattern_check("(!@#$%^&*()",")(*)") == True
```