```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and vice versa.
    Returns a strings with all characters lowercase or uppercase.
    """

def test_flip_case():
    """This function tests the flip_case function by providing input strings and checking the output."""
    assert flip_case('hello') == 'HElLo'
    assert flip_case('helloWorld!') == 'helloWOrld'
    assert flip_case('to bee ORd') == 'eorD'
    assert flip_case('altzHeIZ') == 'I ZavE'
    assert flip_case('suspicious! manufacturing!') == 'usnoxin
    """ passes all test cases, and is called to test its own function."""
def main():
    print(f'Testing the {test_flip_case()} function.')
if __name__ == "__main__":
    main()
```