```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}{"*n+1}

    def test_string_sequence():
        assert str(string_sequence(0)) == '0', "First test failed"
        assert str(string_sequence(5)) == '0 1 2 3 4 5'
        assert str(string_sequence(10)) == '0 10 20 30 40 50'
        assert str(string_sequence(15)) == '0 15 20 25 30 35'
        assert str(string_sequence(20)) == '0 20 40 60 80'
        assert str(string_sequence(30)) == '0 30 60 90 120'
        assert str(string_sequence(35)) == '0 35 80 105 215'
        assert str(string_sequence(40)) == '0 40 80 160 240'
        assert str(string_sequence(45)) == '0 45 120 270 360'
```