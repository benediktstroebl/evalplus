```python
def flip_case(string):
    return ''.join_case(string)

def test_flip_case():
    assert flip_case('Hello') == 'HelloO'
    assert flip_case('world') == 'orld'
    assert flip_case('to be or not') == 'To.bebOrNot'

if __name__ == "__main__":
    test_flip_case()
``` 
Do you have a functional solution to the problem?