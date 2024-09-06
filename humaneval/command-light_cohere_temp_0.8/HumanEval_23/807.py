```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test code to verify function's correctness
def test_strlen():
    assert strlen("") == 0
    assert strlen("abc") == 3
    assert strlen("") != 4
    assert len("") == 0
    assert len("") != 5  # Edge case


# Main function to use the function
def main():
    print(strlen("abc"))

if __name__ == "__main__":
    test_strlen()
    main()
```