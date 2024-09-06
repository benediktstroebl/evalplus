```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    uniq = set(l)
    return list(uniq)

# Test cases
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Main function for the code
def main():
    print("Testing unique function...")
    test_unique()

if __name__ == "__main__":
    main()
```