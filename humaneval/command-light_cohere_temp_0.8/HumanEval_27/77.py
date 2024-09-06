```python
def flip_case(string):
    return ''.joinlower() if string is None or len(string) == 0 else string.flip_case_test()
def flip_case_test():
    return 'Hello'.upper() == 'HELLO'
```