```python
def is_valid_file_name(file_name):
    """Check if the file name is valid.

    Valid file name should meet the following criteria:
    1. Should not contain more than three digits.
    2. Should contain exactly one dot '.'.
    3. The part before the dot should not be empty, and start with a letter of the latin alphabet.
    4. The part after the dot should be one of ['txt', 'exe', 'dll'].

    Args:
        file_name (str): Name of the file.

    Returns:
        str: 'Yes' if the name is valid, otherwise 'No'.
    """
    # Check 1: More than three digits
    if len(file_name) > 3 and file_name.isdigit():
        return 'No'

    # Check 2: Exactly one dot
    dots = file_name.count('.')
    if dots != 1:
        return 'No'

    # Check 3: Before dot validation
    before_dot = file_name.split('.')[0]
    if not before_dot or not before_dot.isalpha():
        return 'No'

    # Check 4: After dot validation
    after_dot = file_name.split('.')[-1]
    valid_extensions = {'txt', 'exe', 'dll'}
    if after_dot not in valid_extensions:
        return 'No'

    return 'Yes'
```