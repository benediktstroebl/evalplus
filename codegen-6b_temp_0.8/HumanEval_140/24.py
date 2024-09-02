
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    
    text = text.replace(' ', '_')
    
    if text.count('_') > 2:
        text = text.replace('_', '-')
    
    return text

"""
ch-38
	When you try to run the code below, it does not do anything. 
	Which is true for tests that makes use of the random number 
	module, but it's actually not true for tests that use other 
	modules such as datetime. 
	
	Add a line of code below so that when you run the code below, 
	it does not fail.
"""
