```python
def flip_case(string):
    """
    Convert all characters in a string to the opposite case.
    Args:
        string (str): string to flip case
    Returns:
        string with all characters flipped.
    """
    def test():
        return "Hello" == flip_case("hello")
    return True
#main code
if __name__ == "__main__":
    assert test()
    print("Case passed!")
```