
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
    text = text.replace(' ', '_').replace('  ','_')
    # add space after a word is properly capitalized 
    # to ensure that _Example_3 is not replaced by Example_3
    return ' '.join([word if word.isupper() else word.capitalize() for word in text.split('_')])
