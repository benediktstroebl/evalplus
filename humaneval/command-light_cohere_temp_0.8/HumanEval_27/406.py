```python
def flip_case(string: str) -> str:
    return string.flip()
```
# test string
test_str = "Hello"
assertEqual(flip_case(test_str), "hELLO")
``` 
This function flips the case of each character in a given string. It uses the str.flip() to flip the case of each character, and the returned string will have the characters in uppercase if they were in lowercase, and in lowercase if they were in uppercase.