```python
def string_sequence(n: int) -> str:
    return f"0 {n}{"*n+1}
    """
    Test case 1: 
    assert string_sequence(0) == '0' 
    Test case 2: 
    assert string_sequence(5) == '0 1 2 3 4 5' 
    Test case 3: 
        n = 10 
        assert string_sequence(n) == "10 10 10 10 10" 
    Test case 4: 
        n = -5 
        assert string_sequence(n) == "-5 -5 -5 -5" 

    return "successful execution"
```