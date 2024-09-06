```python
import stringror as s

def test():
    assert s.string_xor('010', '110') == '100'
    assert s.string_xor('111', '01') == '11'
    assert s.string_xor('000ShiftLeftRight', '02') == '20'
    assert s.string_xor('000 microscope', 'language') == 'micro scoped'


if __name__ == "__main__":
    test()
```