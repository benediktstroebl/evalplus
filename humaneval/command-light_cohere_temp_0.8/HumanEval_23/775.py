```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

#Test case 1
def test_strlen():
    assert strlen('') == 0 

#Test case 2
def test_strlen():
    assert strlen('abc') == 3 

# Main function
if __name__ == "__main__":
    # Test cases
    test_strlen()
    print("Test cases passed")
```