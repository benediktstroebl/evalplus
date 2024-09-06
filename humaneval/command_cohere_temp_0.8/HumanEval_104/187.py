```python
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Use a dictionary to count the occurrence of each digit
    digit_dict = {}
    for digit in range(0, 10):
        digit_dict[digit] = 0
    
    for num in x:
        for digit in str(num):
            digit_dict[int(digit)] += 1
            
    # Use a set to store digits that are even
    even_digits = set([0, 2, 4, 6, 8])
    
    # Filtering criteria to select numbers without any even digit
    def has_no_even_digit(num):
        for digit in str(num): 
            if int(digit) in even_digits and digit_dict[int(digit)] > 0:
                return False
        return True
            
    # Sorting criteria
    def sort_key(num):
        return int(num)
    
    return sorted(filter(has_no_even_digit, x), key=sort_key)
``` 

The test cases ensure the logic works correctly for different scenarios. You can add more test cases to cover other edge cases. If you prefer, I can provide an additional version of the code with comments explaining each line. Let me know if you would like me to explain any part of the code further.