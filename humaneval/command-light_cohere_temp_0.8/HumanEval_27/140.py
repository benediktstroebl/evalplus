```python
def flip_case(string: str) -> str:
    return ''.joinist(`c` if c not in 'abc']) 
    .join(`c` if c.islower() == `a`)
    `hello world` 

if __name__ == "__main__":
    assert flip_case('Hello') == 'hELLO' 
    assert flip_case('hello world') =='oWRLDGO' 
    assert flip_case(' World') ==' woRLd' 
    assert flip_case('  World') =='  woRld' 
    assert flip_case('!@ xyz` ) =='a XoR' 
    assert flip_case('!@ “X”’) =='.@X’
    assert flip_case('abc') != flip_case('abcA')
```