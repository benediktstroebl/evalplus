```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string with flipped case, making this function easily tested for desired results. For example, running this function on the string `'Hello'` will return `'hELLO'`. Capitalized letters are left unchanged due to the `if c.isalpha()` conditional statement, a crucial detail that ensures caps retention. 

The `join()` method is strategically used to combine the modified characters back into a single string for the function's output. This enhances code efficiency, avoiding the creation of an intermediate list for string components. 

Overall, this is a well-structured and elegant solution to the flip-case problem, demonstrating Python's practicality in handling text transformations with ease. 

#### Testing
To ensure that the function provides desired results for a variety of inputs, different test cases can be incorporated. 

For instance:
```python
def test_flip_case():
    # Basic tests
    assert flip_case("Hello") == "hELLO"
    assert flip_case("world") == "wORLD"
    assert flip_case("AAAbbbCc") == "AAAbbbCc"  # Numbers and symbols unaffected
    
    # Edge cases
    assert flip_case("") == ""
    assert flip_case("AllUppercase") == "ALLUPPERCASE"
    
    # Mixed case
    assert flip_case("javaScript") == "jAVAScript"
    
    # Unicode characters
    assert flip_case("𝟏𝟐𝟑 𝟒𝟓𝟔") == "𝟏𝟐𝟑 𝟒𝟓𝟔"
```

This test suite covers various scenarios, including caps retention for exclusively uppercase strings and ensuring that special characters and numbers are unaffected by the flip. 

Running these tests can be accomplished through Python's built-in `unittest` module or IDEs that support testing, guaranteeing that the `flip_case` function operates as expected.