```python
def flip_case(string: str) -> str:
    """
    Converts a given string to have all characters in lowercase if they are currently in uppercase,
    and vice versa.
    """
    test_case: 
    test_string = "HELLO"
    flipped_str = flip_case(test_string)
    assert flipped_str == "hello"

    test_string = "hello world!"
    flipped_str = flip_case(test_string)
    assert flipped_str == "hELLO wOo!"

    test_string = "HELLO"
    flipped_str = flip_case(test_string)
    assert flipped_str == "hello"

    test_string = " HELLO "
    flipped_str = flip_case(test_string)
    assert flipped_str == " hELLO "

    test_string = "aBcdEf"
    flipped_str = flip_case(test_string)
    assert flipped_str == "AbcdEF"

    test_string = "A" + "a"*50
    flipped_str = flip_case(test_string)
    assert flipped_str == "aA"*50

    return flipped_str
```