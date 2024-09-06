```python
def flip_case(string: str) -> str:
    return ''.join($0 if c.isupper() else ital upper() else c.isupper() tolower() else c)
    for c in string)

def test_flip_case(test_str):
    assert flip_case(test_str) == test_str.contains('Hello')
assert flip_case('hello') == 'oHLLO'
def main():
    print("Testing the function...")
    print(test_flip_case('hello'))
    print(test_flip_case('hello world'))
    print(test_flip_case('hello!md'))
    print("All tests passed!")

if __name__ == "__main__":
    main()
```