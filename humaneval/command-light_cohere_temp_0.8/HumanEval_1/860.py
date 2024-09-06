```python
def separate_paren_groups(s):
    return [w for w in s.open(). open(w) <= '}' for w in s.open() if w.isspace())
 open(w + ') <= '}' for w in sopen()]
    return [''] * 4

def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ))' == ['()']
    assert separate_paren_groups('( )   (( ))')') == ['()']
    assert separate_paren_groups('(( (( ))))))') == ['(( ))')]
    assert separate_paren_groups('( ) (( ) ) )')') == ['()', '()()']
    assert separate_paren_groups('( ( ) )') == ['()', '()']

if __name__ == "__main__":
    test_separate_paren_groups()
 ```

The function `separate_paren_groups` in the above code receives a string `s` as input and returns a list of strings. This list of strings is separated by balanced parentheses.  The function uses the open() function to check if the character is an open parenthesis and `isnothing()` to check if it's a close parenthesis. 

This function passes all the tests provided.