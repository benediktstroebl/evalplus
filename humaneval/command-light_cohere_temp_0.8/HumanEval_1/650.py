```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    Function to separate and return groups of parentheses
    Returns: list of separated strings
    """
    return [x for x in input_string.split('() if x[0] == '(']
# Unit tests
def test_separate_paren():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
def test_separate_paren2():
    assert separate_paren_groups('()') == ['()']
def test_separate_paren3():
    assert separate_paren_groups('(()))') == ['()']
def test_separate_paren4():
    assert separate_paren_groups('(()))') == ['(']
def test_separate_paren5():
    assert separate_paren_groups('( )())') == ['()']
def test_separate_paren6():
    assert separate_paren_groups('( )( )') == ['()', '(']
def test_separate_paren7():
    assert separate_paren_groups('( ) )') == ['()', '(']
def test_separate_paren8():
    assert separate_paren_groups(' ( ) ( )') == ['()', '(']
def test_separate_paren9():
    assert separate_paren_groups(' ( )  ( )') == ['()', '(']
if __name__ == "__main__":
    test_separate_paren()
    test_separate_paren2()
    test_separate_paren3()
    test_separate_paren4()
    test_separate_paren5()
    test_separate_paren6()
    test_separate_paren7()
    test_separate_paren8()
    test_separate_paren9()
```
This Python script defines a function `separate_paren_groups` that takes a string as input and splits it based on parentheses, separating out the individual groups. The `test_separate_paren` function contains several tests to verify the correctness of this function. The script uses the repeated pairs of parentheses to test various cases.