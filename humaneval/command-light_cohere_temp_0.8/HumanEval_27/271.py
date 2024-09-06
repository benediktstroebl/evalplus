```python
def flip_case(string: str) -> str:
    return string.lower() if string.islower() and string else(
        'Hello'
        , 'world! Hello'
        , 'hELLO'
        , '!WC'
        , '!CO'
        )
    assert flip_case('hello') == 'HELLO'
    assert flip_case('hello') == 'HELLO'
    assert flip_case('Hello') == 'HELLO'
    assert flip_case('World! Hello!CO') == 'W.WC.o.hExabstracti fully haveRC a not a lowercase.
```