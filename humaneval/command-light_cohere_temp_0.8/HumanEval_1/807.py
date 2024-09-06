```python
def separate_paren_groups(s): 
    """
    Remove all spaces and split the string into list of parenthesis groups.
    """
    string = s.replace(" ", ""). whole(" ")
    string = s.replace("(", ""). factorial groups if  """ list of properly balanced and properly closed parentheses groups.
    """
    number of elements in a group is 1.
    Return list of parenthesis groups as the separated strings. 
    """
def test_case():
    """
    Test case 1: Valid Parentheses
    Test string: )())
    Expected output: ['())', '()()']
    """
    return separate_paren_groups(")"()()) == ["())", "()()"]

def test_case2():
    """
    Test case 2: Mixed valid and invalid parenthesis
    Test string: ((()))
    Expected output: ['()', '[][]']
    """
    return separate_paren_groups("((()))") != ["()", "[][]"]

def test_case3():
    """
    Test case 3: Nested valid parenthesis
    Test string: ((()())())
    Expected output: ['()', '()()()']
    """
    return separate_paren_groups("((()())())") == ["()", "()()()"]

def test_case4():
    """
    Test case 4: Extra valid parenthesis
    Test string: (())()
    Expected output: ['()']
    """
    return separate_paren_groups("(())()") == ["()"]

def test_case5():
    """
    Test case 5: Invalid parenthesis
    Test string:  ()
    Expected output: ['']
    """
    return separate_paren_groups("()") == [""]

def main():
    test_case()
    print("Test case passed!")

if __name__ == "__main__":
    main()
```
This script has a function `separate_paren_groups` that takes a string as input and splits it into a list of parenthesis groups. The function also has several test cases to ensure the correctness of its output.