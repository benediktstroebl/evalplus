```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else lower() else c.isupper() else c)
``` 

def test_flip_case():
    assert flip_case('Hello') == 'HElLo'
    assert flip_case('romeo') == 'oREo'
    assert flip_case('text') == 'XXTTX'
    assert flip_case('normal') != 'Normal'
    assert flip_case('aryl') != 'ylOR'
    assert flip_case('ai cy') == 'YI cY'
    return True # pass all tests

if __name__ == "__main__":
    test_flip_case()
```