```python
def correct_bracketing(brackets):
    """ Checks whether a string of opening brackets has a corresponding set of closing brackets.

    Parameters:
    brackets: str
        A string of "(" and ")".

    Returns: bool
        True if every opening bracket has a corresponding closing bracket, False otherwise.

>>> correct_bracketing("(()))")
True
>>> correct_bracketing("()")
True
>>> correct_bracketing("))
True
>>> correct_bracketing("(())")
True
>>> correct_bracketing("))()")
False
>>> correct_bracketing("{((()))}")
True
>>> correct_bracketing("{)()}")
False
```  This function, when given a string of opening brackets, checks whether there's a corresponding set of closing brackets for each opening one.  It also checks the critical to do this for all the opening brackets.