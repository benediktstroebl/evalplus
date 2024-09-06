```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.isalpha() else char for char in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. The `join()` method is used to consolidate this new string by combining all the characters into a single string. 

To achieve this, the `swapcase` method is utilized for alphabetic characters, toggling their case, while non-alphabetic characters are left unchanged, ensuring that numbers or special characters remain unaffected. 

This approach enables the function to gracefully address strings containing a blend of cases and non-alphabetic characters, producing the desired result of flipping case while excluding any unintended side effects. 

To properly test this function under various scenarios, you can create a test suite with different cases, including strings with varying character types and cases. By doing so, you can validate the correctness of the function and confirm its robustness across different inputs. 

Here is an example of how to test this function: 
```python
# Test flip_case function
def test_flip_case():
    # Test string with lowercase and uppercase letters
    assert flip_case("hello World") == "hELLO wORLD"

    # Test string with only lowercase letters
    assert flip_case("hello") == "hELLO"

    # Test string with only uppercase letters
    assert flip_case("HELLO") == "hELLO"

    # Test string with digits and special characters
    assert flip_case("hello123 World!") == "hELLO123 wORLD!"

    # Test string with multiple spaces
    assert flip_case("  hello World  ") == "  hELLO wORLD  "

test_flip_case()
```

This code provides a test suite that covers various scenarios, including strings with different cases, strings with special characters, and strings with multiple spaces. By executing these tests, you can confidently verify the expected behavior of the `flip_case` function.